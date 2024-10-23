<template>
  <div class="text-center mx-auto hidden" ref="content">
    <h1>Weekends getaways to explore</h1>
    <v-sheet class="mx-auto d-flex justity-center align-center" style="background-color: #fcf3f3" :height=height>
      <v-slide-group
        v-model="model"
        class="slide-group-style"
        center-active
        show-arrows
      >
        <v-slide-group-item
          v-for="(destination,index) in shuffledarray"
          :key="index"
          v-slot="{isSelected, toggle}"
          class="slide-group-item"
          >
          <v-card class='destinationStyle' :class="{isSelected:selectedIndex===index}" :color="selectedIndex===index?'rgba(1, 61, 90)':'grey lighten-4'" 
          @click=handleClickCard(destination,index)
          
          >
            <v-img
              :src="destination.src"
              height="250px"
              cover
            ></v-img>
            <v-card-title class="text-center text-h5 mt-5"><a> {{destination.name}}-{{ destination.id }} </a></v-card-title>
                
            <v-card-subtitle>{{destination.location}}</v-card-subtitle>
            <v-card-text
              >{{destination.description}}</v-card-text>
            </v-card
          ></v-slide-group-item
        ></v-slide-group>
    </v-sheet>

    <v-dialog v-model="showDialog" class="feature-dialog" persistent @keydown.esc="showDialog = false">
      <v-card class="feature-card mx-auto rounded-lg">
        <v-row class="my-auto">
          <v-col cols="4" sm="4" md="4">
            <v-img :src="selectedDestination.src" class="feature-img" cover/>
          </v-col>
          <v-col cols="8" sm="8" md="8" >
            <div class="card-content fill-height">
              <div class="d-flex justify-center align-center">
                <v-card-title class="text-h5 my-5">
                  {{ selectedDestination.name }}
                </v-card-title>
                <v-spacer></v-spacer>
                <v-icon class="mr-5 mb-10" @click="showDialog = false">mdi-close</v-icon>
              </div>
              <div>
                <v-card-subtitle class="my-5">{{ selectedDestination.location }}</v-card-subtitle>
                <v-card-text>
                  <strong>Details: </strong><br>{{ selectedDestination.description }} <br/><br/>
                  <strong>Category: </strong> {{ selectedDestination.category }}
                </v-card-text>
              </div>
              <v-spacer></v-spacer>
              <div class="text-center">
                <v-btn id="close-btn-feature" @click="showDialog = false">Close</v-btn>
              </div>
            </div>
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
    <!-- <audio ref="flipSound" src="@/assets/sounds/flip.mp3" /> -->
  </div>
</template> 



<script>
import { throttleFilter } from '@vueuse/core';

export default {
  name: "LandingSlider",
  props: {
    id: {
      type: String,
      default: "",
    },
    height: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      showDialog: false,
      shuffledarray: [],
      model: null,
      selectedDestination: {},   
      isOn: false,
      selectedIndex: null,
      destinations : [
        {id : 1,
          src:"src/assets/LandingCarousel/1.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        },
        {id : 2,
          src:"src/assets/LandingCarousel/3.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        category: "Culture Shock",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        },
        {id : 3,
          src:"src/assets/LandingCarousel/3.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        category: "Culture Shock",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        },
        {id : 4,
          src:"src/assets/LandingCarousel/2.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        category: "Culture Shock",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        },
        {id : 5,
          src:"src/assets/LandingCarousel/5.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        category: "Culture Shock",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        },
        {id : 6,
          src:"src/assets/LandingCarousel/2.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        category: "Culture Shock",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        },
        {id : 7,
          src:"src/assets/LandingCarousel/4.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        category: "Culture Shock",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        },
        {id : 8,
          src:"src/assets/LandingCarousel/6.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        category: "Culture Shock",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        },
        {id : 9,
          src:"src/assets/LandingCarousel/6.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        category: "Culture Shock",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        },
        {id : 10,
          src:"src/assets/LandingCarousel/5.jpg",
        name: "Batu Caves",
        location: "Kuala Lumpur",
        category: "Culture Shock",
        description: "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
        }
      ]
    }
  },
  methods: {

    shuffle(array) {
      let currentIndex = array.length;
      while (currentIndex !== 0) {
        let randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;
        [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]];
      }
      return array
    },

    handleClickCard(destination,index) {
      this.selectedDestination = destination;
      this.showDialog = true;
      this.selectedIndex = index;
      this.isCardSelected = true
      }
  },
  mounted() {
    this.shuffledarray = this.shuffle(this.destinations)
    const options = {
      root: null,
      threshold: 0.4,
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("show");
        } else {
        entry.target.classList.remove("show");
      }
      });
    }, options);

    observer.observe(this.$refs.content);
  }
};
</script>

<style scoped>
.hidden {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.show {
  opacity: 1;
  transform: translateY(0);
}

.isSelected {
  transform: scale(1.15);
  position: relative;
  transition: transform 0.1s ease-in-out;
  z-index: 100;
  border-radius: 10px !important;

}
.slide-group-style {
  height: 100%;
  justify-content: center;
  display: flex;
  align-items: center;
}
/* 
.slide-group-item {
  overflow: visible !important; 
  z-index: 1;
  
} */

.v-sheet {
  overflow: visible !important; 
  position: relative; 
}

.destinationStyle {
  margin: 30px 20px 30px 20px;
  border-radius: 10px;
  width: 250px;
  height: 400px;
}

#close-btn-feature {
  background-color: rgba(1, 61, 90);
  color: white;
  width: 30%;
  margin-top: 10px;
  margin-bottom: 10px;
  align-items: center;
}

.feature-img {
  padding: 20px; 
  margin-left: 20px;
  width: 500px;
  height: 450px;
  border-radius: 10px;
}

.card-content {
  justify-content:  space-between;
  flex-direction: column;
  display: flex;
}
</style>
