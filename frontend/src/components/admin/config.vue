<template>
    <b-container>
        <b-row>
            <b-col>
                <h3>Config:</h3>
                <b-form>
                    <b-form-group label="Room rows" id="email_type">
                        <b-form-input type="number" v-model="config.room_raws"></b-form-input>
                    </b-form-group>

                    <b-form-group label="Room Columns" id="email_type">
                        <b-form-input type="number" v-model="config.room_columns"></b-form-input>
                    </b-form-group>

                    <b-form-group label="Registration status:" id="email_type">
                        <b-form-checkbox v-model="config.reg_active">
                            <p v-if="config.reg_active">Rejetracja jest teraz aktywna !</p>
                            <p v-if="!config.reg_active">Rejetracja nie jest teraz aktywna !</p>
                        </b-form-checkbox>
                    </b-form-group>

                    <div class="form-actions">
                        <b-btn variant="primary" @click.prevent="save_config()">Update</b-btn>
                    </div>
                </b-form>
            </b-col>
            <b-col>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "admin_config",
        data() {
            return {
                dataLoading: false,
                config: {}
            }
        },
        created() {
            let self = this;
            axios.get('/admin/config').then((resp) => {
                    self.config = resp.data;
                }
            );
        },
        methods: {
            save_config() {
                let self = this;
                axios.post('/admin/config', self.config).then((resp) => {
                    self.$swal({
                        title: resp.data.msg,
                        type: 'success'
                    });
                });
            }
        }
    }
</script>

<style scoped>

</style>