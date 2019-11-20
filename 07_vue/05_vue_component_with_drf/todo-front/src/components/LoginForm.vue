<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>

    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="error-list alert alert-danger" role="alert">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>
      </div>

      <div class="form-group">
        <label for="id">ID</label>
        <input 
          type="text" 
          class="form-control" 
          id="id" 
          placeholder="아이디를 입력해주세요."
          v-model="credentials.username"
          >
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input 
          type="password" 
          class="form-control"
          id="password" 
          placeholder="비밀번호를 입력해주세요."
          v-model="credentials.password"
          >
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'
  import router from '../router'

  export default {
    name: 'LoginForm',
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        },
        // loading: false,
        errors: [],
      }
    },
    computed: {
      loading: function() {
        return this.$store.state.loading
      }
    },
    methods: {
      login() {
        if (this.checkForm()) {
          // this.loading = true
          this.$store.dispatch('startLoading')
          axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
          .then(res => {
            // this.$session.start()
            // this.$session.set('jwt', res.data.token)
            this.$store.dispatch('endLoading')
            this.$store.dispatch('login', res.data.token)
            router.push('/')
          })
          .catch(err => {
            // this.loading = false
            this.$store.dispatch('endLoading')
            console.log(err)
          })
        } else {
          console.log('로그인 검증 실패')
        }
      },
      checkForm() {
        this.errors = []

        if (!this.credentials.username) {
          this.errors.push("아이디를 입력해주세요.")
        }
        if (this.credentials.password.length < 8) {
          this.errors.push("비밀번호는 8자 이상 입력해주세요.")
        }
        if (this.errors.length === 0) {
          return true
        }
      }
    },
  }
</script>

<style>

</style>
