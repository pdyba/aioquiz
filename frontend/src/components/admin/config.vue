<template>
    <div class="container" xmlns="http://www.w3.org/1999/html">

        <div class="col-md-6 col-md-offset-3">
            <h3>Config:</h3>
            <form name="form"  role="form">


                <div class="form-group"
                     >
                    <label for="room_raws">Raws</label>
                    <p>You need to input 1 and 9999</p>

                    <input name="room_raws" id="room_raws" type="number" v-model="config.room_raws"
                           v-pattern="/^[0-9]{1,4}$/"/>
                </div>

                <div class="form-group"
                     >
                    <label for="room_columns">Columns</label>
                    <span 
                          class="help-inline alert-danger">
                    <p>You need to input 1 and 9999</p>
                </span>
                    <input name="room_columns" id="room_columns" type="number" v-model="config.room_columns"
                           v-pattern="/^[0-9]{1,4}$/"/>
                </div>


                <div class="checkbox">
                    <label for="reg_active">
                        <input type="checkbox" name="reg_active"
                               id="reg_active"
                               v-model="config.reg_active"/>
                        <p v-if="config.reg_active">Rejetracja jest teraz aktywna !</p>
                        <p v-if="!config.reg_active">Rejetracja nie jest teraz aktywna !</p>
                    </label>
                </div>

                <div class="form-actions">
                    <button type="submit"
                            class="btn btn-primary">Update
                    </button>
                    <img v-if="dataLoading"
                         src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA=="/>
                </div>
            </form>
        </div>
    </div>


</template>

<script>
    export default {
        name: "admin_config",
        data: () => {
            return {
                dataLoading: false,
                config: {
                    room_rows: 1,
                    room_columns: 1,
                    reg_active: true
                }
            }
        }
    }
</script>

<style scoped>

</style>