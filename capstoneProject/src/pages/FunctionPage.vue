<template>
  <div>
    <h1>Function Page</h1>
    <p>Selected State: {{ stateArray }}</p>
    <p>Selected Activity: {{ activityArray}}</p>
    <p>Selected Name: {{ destArray }}</p>
  </div>
  <!-- <div>HI</div> -->
 <h1>{{stateTitle}}</h1> 
  <div v-for="destination in destinationFilter" :key="destination.id">
    <DestinationCard :destination="destination" height="200px"/>
  </div>
</template>

<script>
import DestinationCard from "@/components/DestinationCard.vue";
import { useMapState } from "@/stores/mapStores";
import destinationAll from "@/assets/Updated_destination.json";
import { map } from "leaflet";
const mapStore = useMapState();

export default {
  name: "FunctionPage",
  components: {
    DestinationCard
  },
  data() {
    return {
      stateArray: [mapStore.stateFilter],
      activityArray: [mapStore.activityFilter],
      destArray: [mapStore.destionationFilter],
      destinationFilter: [],
      filteredData: [],
      stateTitle: ""
    }
  },

  mounted() {
    console.log(destinationAll);  
    let filteredData = destinationAll.filter((destination) => {
      (this.stateArray !== '' || this.stateArray.includes(destination.state)
      && this.activityArray !== '' || this.activityArray.includes(destination.activity)
      && this.destArray !== '' || this.destArray.includes(destination.name))
    })
    console.log(filteredData,this.stateArray, this.activityArray, this.destArray);
    // if (this.activityArray[0] !== "") {
    //   this.destinationFilter = destinationAll.filter((destination) => destination.activity.includes(this.activityArray))
    // }

    // if (this.stateArray[0] !== "") {
    //   this.destinationFilter = destinationAll.filter((destination) => destination.state.includes(this.stateArray))
    //   this.stateTitle = this.stateArray
    // }

    // if (this.destArray[0] !== "") {
    //   this.destinationFilter = destinationAll.filter((destination) => destination.name.includes(this.destArray))
    // } 

    // if(this.stateArray[0] === "" && this.activityArray[0] === "" && this.destArray[0] === "") {
    //   this.destinationFilter = destinationAll 
    // }
    

    // this.destinationTotal = destinationAll
    // this.destinationTotal.forEach((destination) => {
    //   // console.log(this.activityArray);
    //   // console.log(destination.state.includes(this.stateArray));  
    //   // console.log(destination.state.includes(this.stateArray[0]))
    //   if (this.activityArray[0] !== "")  {
    //     // this.destinationFilter = []
    //     this.destinationFilter.push(destination)
    //     console.log('test 1');
    //   }
    //     else if (this.stateArray[0] !== "") {
    //       // this.destinationFilter = []
    //       this.destinationFilter.push(destination)
    //       console.log(this.destinationFilter.filter((destination) => destination.state.includes('Selangor')));
    //       console.log('test 2');
          
    //     }
    //     else if (this.destArray[0] !== "") {
    //     // this.destinationFilter = []
    //     this.destinationFilter.push(destination)
    //     console.log('test 3');
    //   }
    // })
    // console.log(this.destinationTotal);
    // console.log(this.destinationFilter);
  }
}
</script>
