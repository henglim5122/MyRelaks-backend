<template>
    <div v-for="(profile,index) in profiles" :keys="index" id="profile-card">
    <v-card :width="width" :height="height">
        <v-img :src="profile.src" id="profile-img" cover/>
        <v-dialog width="400px">
            <template v-slot:activator="{ props: activatorProps }">
                <v-btn id="profile-name" v-bind="activatorProps"> {{ profile.name }}</v-btn>
            </template>
            <template v-slot:default="{isActive}">
                <v-card height="300px" class="custom-card">
                    <v-card-title class="custom-text" id="profile-title"> {{ profile.name }}</v-card-title>
                    <v-card-text class="custom-text">I am {{profile.name}}, a {{ profile.age }} year-old {{ profile.job }} from {{ profile.location }}. {{ profile.description }}.</v-card-text>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                    text="Close Dialog"
                    @click="isActive.value = false"
                    color="primary"
                    variant="flat"
                    ></v-btn>
                    </v-card-actions>
                </v-card>
            </template>
        </v-dialog>
    </v-card>
    </div>
</template>

<script>
export default {
    name: "profileCard",
    props: {
        profiles: {
            type: Array,
            default: [],
        },
        height: {
            type: String,
            default: "",
        },
        width: {
            type: String,
            default: "",
        },
    },
    }
</script>

<style scoped>

#profile-card{
margin: 20px;
}

#profile-img {
    height: 90%;
}

#profile-name {
    height: 10%;
    width: 100%;
}

#profile-title {
    font-size: 30px;
    margin-top: 20px;
    text-align: center;
}

.profile-info {
    margin: auto;
}

.custom-card .custom-text {
    color: black;
    text-align: center;

}

</style>