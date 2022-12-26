const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const merge = require('merge-stream');
const rename = require('gulp-rename');
const cleanCSS = require('gulp-clean-css');
const sourcemaps = require('gulp-sourcemaps');
const autoprefixer = require('gulp-autoprefixer');
const spawn = require('child_process').spawn;
const javascriptObfuscator = require('gulp-javascript-obfuscator');

const installed_apps = ['news'];

gulp.task('serve:backend', function () {
    let devServerPort = process.env.PORT || 8000;
    process.env.PYTHONUNBUFFERED = 1;
    process.env.PYTHONDONTWRITEBITECODE = 1;
    spawn('python', ['manage.py', 'runserver', 'localhost:' + devServerPort], {
        stdio: 'inherit'
    });
});


gulp.task('styles', function () {
  let tasks = installed_apps.map((app) => {
    return gulp
      .src('apps/' + app + '/static_src/scss/**/*.scss')
      .pipe(sourcemaps.init())
      .pipe(sass({ outputStyle: 'compressed' }).on('error', sass.logError))
      .pipe(rename({ suffix: '.min', prefix: '' }))
      .pipe(autoprefixer())
      .pipe(cleanCSS({ compatibility: 'ie8' }))
      .pipe(sourcemaps.write())
      .pipe(gulp.dest('apps/' + app + '/static/' + app + '/css'));
  });

  return merge(tasks);
});

gulp.task('scripts', function () {
  let tasks = installed_apps.map((app) => {
    return (
      gulp
        .src('apps/' + app + '/static_src/js/**/*.js')
        .pipe(sourcemaps.init())
        .pipe(javascriptObfuscator({compact: true}))
        .pipe(rename({ suffix: '.min', prefix: '' }))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('apps/' + app + '/static/' + app + '/js'))
    );
  });

  return merge(tasks);
});

gulp.task('watch', function () {
  gulp.watch(
    installed_apps.map((app) => 'apps/' + app + '/static_src/scss/**/*.scss'),
    gulp.parallel('styles')
  );
  gulp.watch(installed_apps.map((app) => 'apps/' + app + '/static/js/**/*.js'), gulp.parallel('scripts'));
});

gulp.task('default', gulp.parallel('watch', 'styles', 'scripts'));