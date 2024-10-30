<template>
  <v-app>
    <NavigationBar />
  <v-main>
  <div id="AboutUs" height="800px">
    <h1 class="mx-auto text-center pt-7">About Us</h1>
    <div class="AboutUs">
      <p class="my-7">
        We are a dynamic and adventurous team dedicated to showcasing the beauty
        of Malaysia. From the stunning beaches to the vibrant cities, we are
        passionate about helping travelers discover unique experiences across
        this incredible country. Our mission is to make every trip memorable,
        offering personalized recommendations and insider tips for exploring
        hidden gems and popular attractions alike. Whether you're seeking
        relaxation or adventure, we're here to guide you every step of the way!
      </p>
    </div>

    <div id="profile-grid">
      <ProfileCard :profiles="profiles" height="400px" width="200px" />
    </div>
  </div>
</v-main>
  </v-app>
</template>

<script>
export default {
  name: "AboutUs",
  data() {
    return {
      profiles: [
        {
          src: "src/assets/ProfileImage/fizan.jpg",
          name: "Fizan",
          age: "28",
          job: "Software Engineer",
          location: "Kuala Lumpur",
          description: "I'm passionate about back end development",
        },
        {
          src: "src/assets/ProfileImage/deshika.jpg",
          name: "Deshika",
          age: "23",
          job: "Data Analyst",
          location: "Kuala Lumpur",
          description: "I'm passionate about back end development",
        },
        {
          src: "src/assets/ProfileImage/sh.jpg",
          name: "Seen Heng",
          age: "29",
          job: "Data Processor",
          location: "Kuala Lumpur",
          description:
            "I'm passionate about both front end and back end development",
        },
        {
          src: "src/assets/ProfileImage/haziq.jpg",
          name: "Haziq",
          age: "29",
          job: "Cloud Engineer",
          location: "Kuala Lumpur",
          description: "I'm passionate about back end development",
        },
        {
          src: "src/assets/ProfileImage/ruben.jpg",
          name: "Kumara Ruben",
          age: "23",
          job: "Front End Developer",
          location: "Kuala Lumpur",
          description: "I'm passionate about front end development",
        },
      ],
    };
  },
};
</script>

<style scoped>
div {
  color: white;
}

#AboutUs {
  background-color: rgba(1, 61, 90);
  margin-top: 20px;
}

.AboutUs {
  width: 50%;
  text-align: justify;
  text-align-last: center;
  justify-content: center;
  margin: auto;
  margin-top: 10px;
}

#profile-grid {
  display: flex;
  margin: 20px;
  justify-content: center;
}
</style>
