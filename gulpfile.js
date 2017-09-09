var gulp = require('gulp');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var templateCache = require('gulp-angular-templatecache');


const version = Array(15)
    .fill('')
    .map(() => 'abcdefghijklmnopqrstuvwxyz0123456789'.charAt(Math.floor(Math.random() * 36)))
    .join('');

const outputDir = './static/dist';

const scripts = [
    './node_modules/angular/angular.min.js',
    './node_modules/jquery/dist/jquery.min.js',
    './node_modules/bootstrap/js/bootstrap.min.js',
    './node_modules/angular-route/angular-route.min.js',
    './node_modules/angular-cookies/angular-cookies.js',

    './static/js/sweetalert.min.js',
    './static/js/SweetAlertAng.min.js',
    './static/js/main.js',
    './static/js/templates.js',
    './static/js/partials.js',
];


gulp.task('concatPartials', () => {
    return gulp.src('static/partials/*html')
        .pipe(templateCache({
            module: 'aioquiz', // must be the same as main module name
            root: 'partials'
        }))
        .pipe(gulp.dest('static/js'));
});


gulp.task('build', () => {
    console.log(`version: ${version}`);
    return gulp.src(scripts)
        .pipe(concat('bundle.js'))
        .pipe(gulp.dest(outputDir))
        .pipe(rename(`bundle.${version}.min.js`))
        .pipe(gulp.dest(outputDir));
});
