<template>
    <div class="mx-auto d-flex justify-center align-center">
    <div id="subscription-container" class="mx-5" v-for="subscription in subscriptionDetail">
        <v-card :height="height" :width="width" class="backgroundStyle cardContainer">
            <div>
            <v-card-title class="subscriptionType">
                {{ subscription.name }}
            </v-card-title>
            <v-card-text class="d-flex align-end justify-center">
                <div class="text-h4 font-weight-bold ">
                    RM&nbsp;{{ subscription.price }}
                </div>
                <div> &nbsp; /3 months  </div>
            </v-card-text>
            <v-card-text>
                <div class="subscriptionBenefit">
                    This plan includes:
                    <div>
                    <ul v-for="benefit in subscription.benefit">
                        <dd>{{ benefit }}</dd>
                    </ul>
                    </div>
                </div>
            </v-card-text></div>
            
            <v-btn class="subscriptionBtn" color="primary" >Subscribe!</v-btn>
        </v-card>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            subscriptionDetail: [{
                name: "Starter",
                price: 14.99,
                benefit: [
                    "10% discount",
                    "Up 5 destinations",
                    "Points system",]
            },
            {
                name: "Intermediate",
                price: 29.99,
                benefit: [
                    "10% discount",
                    "Up 10 destinations",
                    "Points system",
                    "Free Cancellation & Full Refund"]
                
            },
            {
                name: "Pro",
                price: 49.99,
                benefit: [
                    "15% discount",
                    "Up 20 destinations",
                    "Points system",
                    "Free Cancellation & Full Refund",
                    "Exclusive Offers to your favourite destinations",]
            }
            ],

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
    }    
}
</script>

<style scoped>
.backgroundStyle {
    /* background-image: linear-gradient( rgba(154, 161, 165, 0.25), rgba(1, 61, 90),rgba(154, 161, 165, 0.25)); */
    text-align: center;
    margin: auto;
    border-radius: 15px;
    border: 1px solid black;

}

.cardContainer {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding-block: 10px;
}


.subscriptionBenefit {
    text-align: left;
    margin: 0px 20px 0px 20px;
    font-size: large;
    font-weight: bold;
}

.subscriptionBtn {
    width: 60%;
    font-size: medium;
}

dd {
  display: list-item;
  list-style-type: "✨";
  padding-inline-start: 1ch;
  margin-top: 0.5rem;
  font-size: medium;
}

.subscriptionType {
    font-size: 40px;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif ;
    margin-bottom: 3px;
}


</style>