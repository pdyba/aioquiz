<template>
    <container>
        <h1 class="page-header">Lessons</h1>

            <row class="mb-4" className="card-deck" v-for="i in rowCount">
                <column sm="4" v-for="x in itemCountInRow(i)">
                    <card className="samesize card-dark card-cascade">
                        <card-header>{{ x.id }}. {{ x.title }}</card-header>
                        <card-body>{{ x.description }}</card-body>
                        <card-footer>
                            <router-link :to="/lessons/ + x.id">
                            <btn color="primary"> Go! </btn>
                            </router-link>
                        </card-footer>
                    </card>
                </column>
            </row>

    </container>
</template>

<script>
    import axios from 'axios';

    import Container from '../../material_components/Container.vue';
    import Row from '../../material_components/Row.vue';
    import Column from '../../material_components/Col.vue';
    import Card from '../../material_components/Card.vue';
    import CardHeader from '../../material_components/CardHeader.vue';
    import CardBody from '../../material_components/CardBody.vue';
    import CardFooter from '../../material_components/CardFooter.vue';
    import Btn from '../../material_components/Button.vue';


    export default {
        data() {
            return {
                lessons: [],
                itemsPerRow: 3
            }
        },
        components: {
            Container,
            Row,
            Column,
            Card,
            CardHeader,
            CardFooter,
            CardBody,
            Btn
        },
        name: "lessons",
        created() {
            let self = this;
            axios.get('/lessons').then(
                function (response) {
                    self.lessons = response.data;
                }
            );
        },
        computed: {
            rowCount: function () {
                return Math.ceil(this.lessons.length / this.itemsPerRow);
            },
        },
        methods: {
            itemCountInRow: function (index) {
                return this.lessons.slice((index - 1) * this.itemsPerRow, index * this.itemsPerRow)
            }
        }
    }
</script>

<style scoped>

</style>