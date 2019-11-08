<template>
  <div id="app">
    <div class="container">
      <!-- 1-3. 호출하시오. 
        필요한 경우 props를 데이터를 보내줍니다.
      -->
      <movie-list :genres="genres" :movies="movies"></movie-list>
    </div>
  </div>
</template>

<script>
const axios = require('axios');
// 1-1. 저장되어 있는 MovieList 컴포넌트를 불러오고,
import MovieList from "./components/movies/MovieList.vue";

export default {
  name: 'app',
  // 1-2. 아래에 등록 후
  components: {
    MovieList,
  },
  data() {
    return {
      // 활용할 데이터를 정의하시오.
      movies: [],
      genres: [],
    }
  },
  mounted() {
    const genreUrl = 'https://gist.githubusercontent.com/edujunho-hphk/b7d063a9efd11acba51f6dcedcc8c520/raw/d2cae437669b41c7316c426f5451ef34792b9f39/genre.json'
      axios.get(genreUrl)
        .then(response => {
          this.genres = response.data
          this.genres.unshift({
            "id": 0,
            "name" : "전체보기",
          })
      })
    const movieUrl = 'https://gist.githubusercontent.com/edujunho-hphk/1a75dbae2f69a33d1519a8703d5afa5c/raw/05bc2a01ad9ad0338bf67a15be321a1e1858ab4f/movies.json'
    axios.get(movieUrl)
      .then(response => {
        this.movies = response.data
      })
    // 0. mounted 되었을 때, 
    // 1) 제시된 URL로 요청을 통해 data의 movies 배열에 해당 하는 데이터를 넣으시오. 
    // 2) 제시된 URL로 요청을 통해 data의 genres 배열에 해당 하는 데이터를 넣으시오.
    // axios는 위에 호출되어 있으며, node 설치도 완료되어 있습니다.
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
