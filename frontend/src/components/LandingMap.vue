<template>
  <h1 class="mx-auto text-center pb-5">Explore the States</h1>
  <div id="map"></div>
  <!-- <div>{{ stateFilter }}</div> -->
  <div v-if="showDialog" id="stateDialog" class="dialog-overlay border-lg">
    <v-card
      width="500px"
      height="400px"
      class="dialog-content"
      @keyup.esc="showDialog = false"
    >
      <v-card-title class="mx-auto justify-center d-flex text-h3">
        {{ mapStore.stateFilter }}</v-card-title
      >
      <v-card-text style="text-align: justify">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor
        sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
        ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet,
        consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua.
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="StateFilter" class="mx-4 border-sm"
          ><a
            href="/functionpage"
            target="_blank"
            :style="{ textDecoration: 'none', color: 'black' }"
            >Learn More</a
          ></v-btn
        >
        <v-btn
          color="primary"
          variant="flat"
          text="Close Dialog"
          @click="showDialog = false"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script setup lang="ts">
import leaflet from "leaflet";
import { ref, onMounted } from "vue";
import { useMapState } from "@/stores/mapStores";
import geofile from "@/assets/map/my.json";
import destinationAll from "@/assets/Updated_destination.json";

let map: leaflet.Map;
let userGeoMarker: leaflet.Marker;
const showDialog = ref(false);

let mapStore = useMapState();

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(
    (position) => {
      const lat = position.coords.latitude;
      const lng = position.coords.longitude;
      console.log(lat, lng);
    },
    (error) => {
      console.error("permission is not allowed");
    }
  );
}

function StateFilter(event: Event) {
  const found = destinationAll.some(
    (destination) => destination.state === mapStore.stateFilter
  );
  if (!found) {
    alert("State not found");
    event.preventDefault();
  }
  showDialog.value = false;
}

function handleEscape(event: any) {
  if (event.key === "Escape") {
    showDialog.value = false;
  }
}

onMounted(() => {
  window.addEventListener("keydown", handleEscape);

  map = leaflet
    .map("map", {
      zoomSnap: 0.1,
    })
    .setView([4.83, 109.07], 6);

  leaflet
    .tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 14,
      minZoom: 1,
      attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    })
    .addTo(map);

  function style() {
    return {
      weight: 2,
      opacity: 1,
      color: "blue",
      dashArray: "3",
      fillOpacity: 0.3,
    };
  }

  let geojson = leaflet
    .geoJSON(geofile as GeoJSON.GeoJsonObject, { style: style })
    .addTo(map);
  let geoprops = geofile.features;

  function highlightFeatureLayer(e: any) {
    let layer = e.target;
    layer.setStyle({
      weight: 3,
      color: "orange",
      dashArray: "",
      fillOpacity: 0.7,
    });
    layer.bringToFront();
  }

  function resetHighlight(e: any) {
    geojson.resetStyle(e.target);
  }
  function zoomToFeature(e: any) {
    map.fitBounds(e.target.getBounds());
  }

  function onEachFeature(feature: any, layer: any) {
    layer.on({
      mouseover: highlightFeatureLayer,
      mouseout: resetHighlight,
      click: zoomToFeature,
    });
  }

  geojson = leaflet
    .geoJson(geofile as GeoJSON.GeoJsonObject, {
      style: style,
      onEachFeature: onEachFeature,
    })
    .addTo(map);

  geoprops.forEach((geoprop) => {
    const popupContent = `<strong>${geoprop.properties.name}</strong><br/>
    <button class='open-dialog-btn-${geoprop.properties.name
      .split(" ")
      .join("")}'><a><h3>Open Details</h3></a></button>
  `;
    const stateMarker = leaflet
      .marker([geoprop.properties.id[0], geoprop.properties.id[1]])
      .addTo(map)
      .bindPopup(popupContent, { closeButton: false });

    stateMarker.on("popupopen", () => {
      const popupElement = document.querySelector(
        `.open-dialog-btn-${geoprop.properties.name.split(" ").join("")}`
      );
      popupElement?.addEventListener("click", () => {
        // let selectedState = geoprop.properties.name;
        mapStore.setStateFilter(geoprop.properties.name);
        mapStore.setactivityFilter("");
        mapStore.setdestinationFilter("");
        // console.log(stateFilter); //state
        showDialog.value = true;
      });
    });
  });

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;

        if (userGeoMarker) {
          map.removeLayer(userGeoMarker);
        }

        var greenIcon = new leaflet.Icon({
          iconUrl:
            "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png",
          shadowUrl:
            "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
          iconSize: [25, 41],
          iconAnchor: [12, 41],
          popupAnchor: [1, -34],
          shadowSize: [41, 41],
        });

        userGeoMarker = leaflet
          .marker([lat, lng], {
            // .marker([userMarker.value.latitude, userMarker.value.longitude], {
            icon: greenIcon,
          })
          .addTo(map)
          .bindPopup("You are here", { closeButton: false })
          .openPopup();
      },
      (error) => {
        console.error("permission is not allowed");
      }
    );
  }

  // if (userGeoMarker) {
  //   map.removeLayer(userGeoMarker);
  // }
  // var greenIcon = new leaflet.Icon({
  //   iconUrl:
  //     "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png",
  //   shadowUrl:
  //     "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
  //   iconSize: [25, 41],
  //   iconAnchor: [12, 41],
  //   popupAnchor: [1, -34],
  //   shadowSize: [41, 41],
  // });
  // userGeoMarker = leaflet
  //   .marker([lat, lng], {
  //   // .marker([userMarker.value.latitude, userMarker.value.longitude], {
  //     icon: greenIcon,
  //   })
  //   .addTo(map)
  //   .bindPopup("You are here",{closeButton: false}).openPopup();
  // ;

  map.addEventListener("click", (e) => {
    const { lat: latitude, lng: longitude } = e.latlng;
    console.log("clicked on", latitude.toFixed(2), longitude.toFixed(2));
  });
});

onBeforeUnmount(() => {
  map.remove();
  document.removeEventListener("keyup", handleEscape);
});
// watchEffect(() => {
//   if (
//     coords.value.latitude !== Number.POSITIVE_INFINITY &&
//     coords.value.longitude !== Number.POSITIVE_INFINITY
//   ) {
//     userMarker.value.latitude = coords.value.latitude;
//     userMarker.value.longitude = coords.value.longitude;

//     if (userGeoMarker) {
//       map.removeLayer(userGeoMarker);
//     }

//     userGeoMarker = leaflet
//       .marker([userMarker.value.latitude, userMarker.value.longitude])
//       .addTo(map)
//       .bindPopup("user marker");

//     const el = userGeoMarker.getElement();
//     if (el) {
//       el.style.filter = "hue-rotate(120deg)";
//     }
//   }
// });
// return stateFilter;
</script>

<style scoped>
#map {
  width: 80%;
  height: 500px;
  margin: auto;
  border-radius: 10px;
}

.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.v-card {
  overflow: auto;
  height: 30%;
}

.dialog-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* Ensures content and buttons are spaced properly */
  border-radius: 10px;
}
</style>
