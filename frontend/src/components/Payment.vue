<template>
  <v-card>
    <div v-if="paymentAmount === 0">
      <v-btn class="closeIcon" @click="$emit('close')"> <v-icon>mdi-close</v-icon></v-btn>
      <h1 class="text-center d-flex justify-center align-center FreemiumContent">
        Enjoy your 1 month subscription starting from today
      </h1>
    </div>
    <div v-if="paymentAmount !== 0">
      <v-tabs v-model="payment" align-tabs="center" stacked>
        <v-tab value="tab-1" width="200">
          <v-icon icon="mdi-card-text" class="mb-2"></v-icon>
          Visa / Debit
        </v-tab>

        <v-tab value="tab-2" width="200" @click="startCountdown">
          <v-icon icon="mdi-qrcode-scan" class="mb-2"></v-icon>
          QR
        </v-tab>
      </v-tabs>
      <v-btn class="closeIcon" @click="$emit('close')"> <v-icon>mdi-close</v-icon></v-btn>
      <v-tabs-window v-model="payment" class="text-center d-flex justify-center align-center">
        <v-tabs-window-item value="tab-1" class="creditCard">
          <!-- <div class="paymentContainer">
          <v-col cols="7" sm="7" md="7">
            <v-row>
              <v-col>
                <div></div>
              </v-col>
            </v-row>
            <v-card-text class="textAlignment"> Card Number </v-card-text>
            <v-row
              ><v-col cols="3" sm="3" md="3" v-for="(value, index) in cardNumber" :key="index">
                <v-text-field
                  required
                  number
                  placeholder="1234"
                  v-model="cardNumber[index]"
                  maxlength="4"
                  @input="checkInput(index)"
                ></v-text-field></v-col
            ></v-row>
            <v-row>
              <v-col>
                <v-card-text class="textAlignment"> Expiry Date </v-card-text>
                <v-row>
                  <v-col v-for="(value, index) in expiryDate" :key="index"
                    ><v-text-field
                      required
                      number
                      v-model="expiryDate[index]"
                      placeholder="01"
                      maxlength="2"
                      @input="checkInputDate(index)"
                    ></v-text-field
                  ></v-col>
                </v-row>
              </v-col>
              <v-col cols=" 3" sm="3" md="3"></v-col>
              <v-col cols=" 3" sm="3" md="3">
                <v-card-text class="textAlignment"> CVV </v-card-text>
                <v-row>
                  <v-col
                    ><v-text-field
                      required
                      number
                      placeholder="123"
                      v-model="security"
                      maxlength="3"
                    ></v-text-field
                  ></v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-col>
        </div> -->

          <v-card class="paymentContainer">
            <div style="overflow: scroll; height: 600px">
              <h2 class="text-center pt-5">Payable Amount: RM {{ paymentAmount }}</h2>
              <CreditCard />
            </div>
          </v-card>
        </v-tabs-window-item>

        <v-tabs-window-item value="tab-2">
          <v-card class="paymentContainer">
            <div style="overflow: scroll; height: 600px">
              <v-card-text>
                <h2 ref="countDownText" class="py-5">
                  Your QR session will be expiring in {{ countdown }} seconds
                </h2>
                <h2 class="text-center py-3">Payable Amount: RM {{ paymentAmount }}</h2>
                <h3 id="countDownText">Please Scan the QR Code</h3>
              </v-card-text>

              <div v-if="countdown > 0" class="QRcodeContainer">
                <v-img height="300px" width="300px" :src="this.image" class="QRcode"></v-img>
              </div>
            </div>
          </v-card>
        </v-tabs-window-item>
      </v-tabs-window>
    </div>
  </v-card>
</template>

<script>
import { ref } from 'vue';
import QrcodeVue from 'qrcode.vue';
import { generateCodeFrame } from 'vue/compiler-sfc';

export default {
  components: {
    QrcodeVue,
  },
  props: {
    subscription: {
      type: Object,
    },
    toPay: {
      type: Boolean,
    },
    paymentAmount: {
      type: Number,
    },
  },
  data() {
    return {
      payment: 'tab-1',
      cardNumber: ['', '', '', ''],
      expiryDate: ['', ''],
      security: '',
      fullName: '',
      card: [],
      countdown: '-',
      timeLeft: 5,
      intervaltime: null,
      images: [
        'src/assets/QR/qr1.png',
        'src/assets/QR/qr2.png',
        'src/assets/QR/qr3.png',
        'src/assets/QR/qr4.png',
      ],
    };
  },
  emits: ['close'],
  methods: {
    checkInput(index) {
      const value = this.cardNumber[index];
      // Trim the value to 4 digits
      if (value.length > 4) {
        this.cardNumber[index] = value.slice(0, 4);
      } else {
        this.cardNumber[index] = value;
      }
    },
    checkInputDate(index) {
      const value = this.expiryDate[index];
      // Trim the value to 4 digits
      if (value.length > 4) {
        this.expiryDate[index] = value.slice(0, 2);
      } else {
        this.expiryDate[index] = value;
      }
    },

    startCountdown() {
      if (this.intervaltime) {
        clearInterval(this.intervaltime);
      }
      this.value = this.generateQRValue();
      this.timeLeft = 5;
      // console.log('hi');
      this.intervaltime = setInterval(() => {
        if (this.timeLeft > -1) {
          this.countdown = this.timeLeft;
          this.timeLeft--;
          this.$refs.countDownText.innerHTML = `Your QR session will be expiring in ${this.countdown} seconds`;
        } else {
          this.$refs.countDownText.innerHTML = 'Session is expired';
          this.refreshComponent();
        }
      }, 1000);
    },
    generateQRValue() {
      this.image = `src/assets/QR/qr${Math.floor(Math.random() * 4) + 1}.png`;
    },
    refreshComponent() {
      this.startCountdown();
    },
  },
  mounted() {
    // this.$refs.countDownText.textContent = `your QR session will be expiring in ${this.countdown} seconds`;
  },
  watch: {
    paymentAmount(newValue, oldValue) {
      console.log('paymentAmount changed from', oldValue, 'to', newValue);
      // Handle the change here (e.g., trigger some action based on the new value)
    },
  },
};
</script>

<style scoped>
.creditCard {
  text-align: left;
}
.paymentContainer {
  width: 1200px;
  height: 600px;
  background-color: white;
}

.FreemiumContent {
  width: 1200px;
  height: 400px;
}
.textAlignment {
  text-align: left;
  /* font-weight: bold; */
  font-size: large;
}

.QRcodeContainer {
  height: 400px;
  align-items: center;
  justify-content: center;
  display: flex;
}

.closeIcon {
  position: absolute;
  top: 0;
  right: 0;
  margin-top: 20px;
  margin-right: 20px;
}
</style>
