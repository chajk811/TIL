## v-model

- input tag 의 value - View <==> v-model <==>data(VM)



## computed

- 미리 계산된 값을 반환

- 종속 대상을 따라 저장(캐싱) 되는 특성이 있다.

- 연상이 많이 필요한 경우. 템플릿 안에서 연산 표현식을 사용하는 것보다 computed를 사용하는 것을 권장

- `{{ newTodo.split('').reverse.join('') }}`

  ``` vue
  computed: {
      reversedNew: function(){
      	return this. newTodo.split('').reverse.join('')
      }
  }
  ```



## View -VM -M(localstorage)



## Watch

- Vue 인스턴스의 data 변경을 관찰하고 이에 반응
- 데이터 변경에 대한 응답으로 비동기 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 적합
- 특정 데이터가 변경되었을때 정의한 함수를 실행.



## v-if / v-show

`v-if` : 조건에 맞지 않으면 렌더링 자체를 하지 않음

`v-show` : 조건과 관계없이 일단 렌더링 후에, 조건에 맞지 않으면 CSS display 속성을 토글해서 숨겨버림.



---

### `v-bind:` => `:`

### `v-on:` => `@`

----

### computed vs watch

computed : 계산해야 하는 `목표데이터를 정의하는 방식`(선언형 프로그래밍)

watch : 감지할 데이터를 지정하고 그 `데이터가 바뀌면 특정함수를 실행하라는 방식`(명력형 프로그래밍)

