var gulp   = require('gulp'),
    sass   = require('gulp-sass');





gulp.task('build-css', function() {
  return gulp.src('source/scss/**/*.scss')
    .pipe(sass())
    .pipe(gulp.dest('static/css'));
});




/* updated watch task to include sass */

gulp.task('watch', function() {
   gulp.watch('source/scss/**/*.scss', ['build-css']);
});