<template>
    <!-- <div class="backgroundColour">
    <div class="subscriptionTitle">Subscription Plan</div> -->
    <div class="mx-auto d-flex justify-center align-center" v-if="isSingle === false">
        <div id="subscription-container" class="mx-5" v-for="subscription in subscriptionDetail">
            <v-card :height="height" :width="width" class="backgroundStyle cardContainer" :style="borderColor(subscription.color)">
                <div id="card-info"  >
                    <v-card-title class="subscriptionType" >
                        {{ subscription.name }}
                    </v-card-title>
                    <v-card-text class="d-flex align-end justify-center">
                        <div class="subscriptionCurrency">
                            RM
                        </div>
                        <div class="text-h3 font-weight-bold ">
                            &nbsp;{{ subscription.price }}
                        </div>
                        <div v-if="subscription.price === 0" class="subscriptionPricePart" > &nbsp; /1 month ONLY</div>
                        <div v-else class="subscriptionPricePart"> &nbsp; /3 months  </div>
                    </v-card-text>
                    <v-card-text>
                        <div class="subscriptionBenefit">
                            This plan includes:
                            <div class="subscriptionDetail">
                            <ul v-for="benefit in subscription.benefit">
                                <dd>{{ benefit }}</dd>
                            </ul>
                            </div>
                        </div>
                    </v-card-text>
                </div>
                <v-btn class="subscriptionBtn" :style="borderColor(subscription.color)">Subscribe!</v-btn>
            </v-card>
        </div>
    </div>

    <div v-if="isSingle === true">Hi</div>
<!-- </div> -->
</template>

<script>
import subscriptionDetail from '@/mock/subscription.json'
export default {
    data() {
        return {
            subscriptionDetail: subscriptionDetail
        }
    },
    props: {
        height: {
            type: String,
            default: "",
        },
        width: {
            type: String,
            default: "",
        },
        tier: {
            type: String,
            default: "",
        },
        isSingle: {
            type: Boolean,
            default: false,
        }

    },
    beforeMount() {
        console.log(subscriptionDetail);
    },
    mounted() {
      console.log('bye');  
    },
    methods: {
        borderColor(color) {
            return {
                "border-color": color
            }
        }
    }    
}
</script>

<style scoped>
/* .backgroundColour {
    background: linear-gradient(to bottom,rgba(1, 61, 90),#fcf3f3);
    padding: 30px 0px 30px 0px;
}
.subscriptionTitle {
    font-size: 65px;
    font-weight: bold;
    letter-spacing: 2px;
    margin-bottom: 30px;
    text-align: center;
    color: white;
    -webkit-text-stroke: 1.5px black;
    
} */


.backgroundStyle:hover{
    border: rgb(231, 167, 90) solid 4px;
    /* transform: scale(1.1); */
}



.backgroundStyle {
    /* background-image: linear-gradient( rgba(154, 161, 165, 0.25), rgba(1, 61, 90),rgba(154, 161, 165, 0.25)); */
    text-align: center;
    margin: auto;
    border-radius: 15px;
    /* border: 0.5px solid grey; */
    box-shadow: 3px 3px 3px 3px rgba(0, 0, 0, 0.2);
}

.cardContainer {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding-block: 10px;
}


#card-info {
    width: 100%;
}

.subscriptionCurrency {
    font-size: x-large;
    font-weight: bold;
}

.subscriptionPricePart {
    /* font-style: italic; */
    font-weight: bold;
    opacity: 0.75;
    color: grey;
}

.subscriptionBenefit {
    width: 90%;
    text-align: left;
    margin: 0px 20px 0px 20px;
    font-size: large;
    font-weight: bold;
}

.subscriptionDetail{
    width: 100%;
}

.subscriptionBtn {
    width: 60%;
    font-size: medium;
    border-radius: 25px;
    background-color: rgba(1, 61, 90);
    margin-bottom: 10px;
    color: white;
}

dd {
  display: list-item;
  list-style-type: "✨";
  padding-inline-start: 1ch;
  margin-top: 0.5rem;
  font-size: medium;
}

.subscriptionType {
    font-size: 35px;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif ;
    margin-bottom: 3px;
    letter-spacing: -0.25px;
    
    
}

#card-info-Starter {
    border: rgb(231, 167, 90) solid 4px;
}

#card-info-Intermediate {
    border: black solid 4px;
}
</style>