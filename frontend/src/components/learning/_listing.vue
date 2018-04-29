<template>
    <b-container>
        <h1 class="page-header">{{ alistingName }}</h1>
            <b-row class="mb-4" className="card-deck" v-for="i in rowCount" :key="i.id">
                <b-col sm="4" v-for="x in itemCountInRow(i)" :key="x.id">
                    <card className="samesize card-dark card-cascade">
                        <card-header>{{ x.id }}. {{ x.title }} <b-badge v-if="x.amount" variant="info">{{ x.amount }}</b-badge></card-header>
                        <card-body>{{ x.description }}</card-body>
                        <card-footer>
                            <router-link :to="'/' + alisting + '/' + x.id">
                            <b-btn variant="primary"> Go!</b-btn>
                            </router-link>
                        </card-footer>
                    </card>
                </b-col>
            </b-row>

    </b-container>
</template>

<script>
    import axios from 'axios';

    import Card from '../common_components/Card.vue';
    import CardHeader from '../common_components/CardHeader.vue';
    import CardBody from '../common_components/CardBody.vue';
    import CardFooter from '../common_components/CardFooter.vue';


    export default {
        data() {
            return {
                listing: [],
                itemsPerRow: 3
            }
        },
        components: {
            Card,
            CardHeader,
            CardFooter,
            CardBody
        },
        props: {
            alisting: {
                type: String,
                required: true
            },
            alistingName: {
                type: String,
                required: true
            }
        },
        name: "listings",
        created() {
            let self = this;
            axios.get('/' + self.alisting).then(
                function (response) {
                    self.listing = response.data;
                }
            );
        },
        computed: {
            rowCount: function () {
                return Math.ceil(this.listing.length / this.itemsPerRow);
            },
        },
        methods: {
            itemCountInRow: function (index) {
                return this.listing.slice((index - 1) * this.itemsPerRow, index * this.itemsPerRow)
            }
        }
    }
</script>

<style scoped>

</style>