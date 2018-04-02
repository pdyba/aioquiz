<template>
    <div>
        <h3>E-Mail:</h3>
        <b-form>
            <b-form-group label="E-mail type:" id="email_type">
                <b-form-select
                        :options="email_options"
                        value-field="email_type"
                        text-field="subject"
                        class="mb-3"
                        name="email_type"
                        @change="email_type_change"
                        size="sm">
                </b-form-select>
            </b-form-group>
            <b-form-group label="To:" id="email_to">
                <b-form-select
                        :options="possible_recipiants"
                        value-field='type'
                        text-field="name"
                        class="mb-3"
                        @change="recipients_type_change"
                        size="sm">

                </b-form-select>
            </b-form-group>
            <b-form-group label="Subject:" id="email_subject">
                <b-form-input
                        type="text"
                        v-model="mail.subject"
                        required>
                </b-form-input>
            </b-form-group>
            <b-form-group label="text:" id="email_text">
                <b-form-textarea
                        v-model="mail.text"
                        required :rows="6">
                </b-form-textarea>
            </b-form-group>
            <div class="form-actions">
                <b-button type="submit" variant="primary" @click.prevent="send_email()">Send</b-button>
            </div>
        </b-form>
    </div>


</template>

<script>
    import axios from 'axios';

    export default {
        name: "admin_send_email",
        data: () => {
            return {
                email_options: {},
                possible_recipiants: [],
                mail: {},
                recipients: {},
                warning: '',
                dataLoading: false
            }
        },
        created() {
            let self = this;
            axios.get('/admin/email').then(
                function (response) {
                    self.email_options = response.data.possible_emails;
                    self.possible_recipiants = response.data.recipients;
                }
            );
        },
        methods: {
            send_email() {
                var self = this;
                axios.post('/admin/email', {
                    "mail": self.mail,
                    "recipients": self.recipients
                }).then(() => swal('Admin: E-mail', 'Email send', 'success'));
            },
            email_type_change(event) {
                this.mail = this.email_options.find((el) => el.email_type === event)
            },
            recipients_type_change(event) {
                this.recipients = this.possible_recipiants[event]
            }
        }
    }
</script>

<style scoped>
</style>