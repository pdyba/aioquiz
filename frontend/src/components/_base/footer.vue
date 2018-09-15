<template>
    <footer>
        <b-container>
            <b-row>
                <b-col sm="6">
                    <a href="#/rules">{{ $t('rules') }}</a>
                    <a href="#/privacy_policy">{{ $t('ppolicy') }}</a>
                </b-col>
                <b-col sm="5">
                    <a class="pull-right" href="https://github.com/pdyba/aioquiz"><i class="fa fa-github"></i>GitHub</a>
                </b-col>
                <b-col sm="1">
                <a class="pull-right">v.{{ version }}</a>
                </b-col>
            </b-row>
        </b-container>
    </footer>
</template>

<script>
    import txt from '../../../../version.txt';
    export default {
        name: 'appFooter',
        data(){
            return {
                version: txt
            }
        }
    }
</script>

<style scoped>

footer {
    margin: 20px 0;
}

</style>


<i18n>
{
  "en": {
    "rules": "Rules",
    "ppolicy": "Privacy Policy"
  },
  "pl": {
    "rules": "Regulamin",
    "ppolicy": "Polityka Prywatności"
  }
}
</i18n>