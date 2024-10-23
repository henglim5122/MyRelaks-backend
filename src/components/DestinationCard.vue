<template>
    <v-card :height="height" :width="width" class="mx-auto rounded-lg my-10">
        <div class="d-flex justfy-center align-center"> 
            <v-card-title class="text-h5">{{ destination.name }}</v-card-title>
            <v-spacer></v-spacer>
            <v-icon class="mr-5" @click="isLiked">
                <v-icon v-if="!onLiked">mdi-cards-heart-outline </v-icon>
                <v-icon v-else class="red-heart">mdi-heart </v-icon>
            </v-icon>
        </div>
        <div>
        <v-card-subtitle><strong>{{ destination.location }}, {{ destination.state }}</strong> ({{ destination.coordinate.latitude }}, {{ destination.coordinate.longitude }})</v-card-subtitle>
        <v-card-text>
            <div class="destinationStyle"  id="destinationDescription" > <strong>{{ destination.description }} </strong></div>
            <div class="destinationStyle">Category: <strong>{{ destination.activityCategory }} </strong></div>
            <div class="destinationStyle" >
                Rating: <i><strong :style="textColor(destination.reviewRating)">{{ destination.reviewRating }}</strong></i> &nbsp;&nbsp;
                <v-rating :model-value="destination.reviewRating" readonly half-increments="true" :length="5" :size="15" active-color="yellow-accent-4" color="grey"></v-rating>
            </div>
            
        </v-card-text>
        </div>
    </v-card>
</template>

<script>
import destination from "@/assets/Updated_destination.json";

export default {
    name: "DestinationCard",
    props : {
            destination: {
                type: Object,
                required: true
            },
            height: {
                type:String,
                default: "",
            },
            width: {
                type:String,
                default: "",
            }},
    data() {
        return {
            onLiked : false
        }
    },
    methods: {
        isLiked() {
            this.onLiked = !this.onLiked;
            this.$emit("onLiked");
            console.log(this.onLiked);  
        },

        textColor(rating) {
            if (rating >= 4.7) {
                return {color:'green'}
            } else if (rating >= 4.4) {
                return {color:'#675e24'}
            } else if (rating >=4.0){
                return {color:'orange'}
            } else {
                return {color:'red'}
            }
        }
    },
    computed: {
        starWidth() {
            // console.log(this.destination.reviewRating/5 * 100);  
            return `${this.destination.reviewRating/5 * 100}%`;
        }
    }
}

</script>

<style scoped>
.v-card {
    width : 80%;
}

.red-heart {
    color: red;
}

.destinationStyle {
    margin-top: 20px;
}

#destinationDescription {
    font-size: larger;
}

</style>