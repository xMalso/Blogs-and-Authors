<template>
    <div>
      <h5>Create New Author</h5>
      <form @submit.prevent="submitAuthor">
        <div class="mb-2">
          <label for="authorName" class="form-label">Author Name</label>
          <input type="text" id="authorName" v-model="author.name" class="form-control" required />
        </div>
        <div class="mb-2">
          <label for="authorBio" class="form-label">Author Bio</label>
          <textarea id="authorBio" v-model="author.bio" class="form-control" required></textarea>
        </div>
        <div class="mb-2">
          <label for="authorAge" class="form-label">Author Age</label>
          <input type="number" id="authorAge" v-model="author.age" class="form-control" required />
        </div>
        <button type="submit" class="btn btn-primary">Create Author</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        author: {
          name: '',
          bio: '',
          age: null
        }
      };
    },
    methods: {
      submitAuthor() {
        if (!this.author.name || !this.author.bio || !this.author.age) {
          alert('Please fill in all fields for the author');
          return;
        }
        this.$emit('submit-author', this.author);
        this.resetForm();
      },
      resetForm() {
        this.author = { name: '', bio: '', age: null };
      }
    }
  };
  </script>
  