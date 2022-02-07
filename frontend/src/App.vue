<template>
  <div id="app">

      <form @submit.prevent="submitForm">
        <div class="row">
          <div class="col-lg-3 my-3">
            <input type="text" class="form-control" placeholder="Name" v-model="student.name">
          </div>
          <div class="col-lg-3 my-3">
            <input type="text" class="form-control" placeholder="Course" v-model="student.course">
          </div>
          <div class="col-lg-3 my-3">
            <input type="text" class="form-control" placeholder="Rating" v-model="student.rating">
          </div>
          <button class="btn btn-success col-lg-3 my-3">Submit</button>
        </div>
      </form>

      <table class="table table-striped">
        <thead>
          <th>Name</th>
          <th>Course</th>
          <th>Rating</th>
        </thead>
        <tbody>
          <tr v-for="student in students" :key="student.id" @dblclick="$data.student=student">
            <td>{{ student.name }}</td>
            <td>{{ student.course }}</td>
            <td>{{ student.rating }}</td>
            <td><button class="btn btn-outline-danger btn-sm mx-1" @click="deleteStudent(student)">x</button></td>
          </tr>
        </tbody>
      </table>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {},
  data() {
    return {
      student: {},
      students: []
    }
  },
  async created() {
    await this.getStudents()
  },
  methods: {
    async getStudents() {
      var response = await fetch('https://app-easyapp.herokuapp.com/api/students/')
      this.students = await response.json()
    },
    submitForm () {
      if (this.student.id === undefined) {
        this.createStudent()
      } else {
        this.editStudent()
      }
    },
    async createStudent() {
      await this.getStudents()

      await fetch('https://app-easyapp.herokuapp.com/api/students/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          
        },
        body: JSON.stringify(this.student)
      })
      await this.getStudents()
    },
    async editStudent() {
      await this.getStudents()

      await fetch(`https://app-easyapp.herokuapp.com/api/students/${this.student.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json',
          
        },
        body: JSON.stringify(this.student)
      })
      await this.getStudents()
      
      this.student = {}
    },
    async deleteStudent(student) {
      await this.getStudents()

      await fetch(`https://app-easyapp.herokuapp.com/api/students/${student.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json',
          
        },
        body: JSON.stringify(this.student)
      })
      await this.getStudents()
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
