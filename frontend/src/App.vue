<template>
    <div class="container pt-3">
      <div class="pb-3">
        <ul>
            <li>
                <button class="nav-link" :class="{active: currentTab === 'contributions'}" @click="currentTab = 'contributions'">Contributions</button>
            </li>
            <li>
                <button class="nav-link" :class="{active: currentTab === 'book'}" @click="currentTab = 'book'">Books</button>
            </li>
            <li>
                <button class="nav-link" :class="{active: currentTab === 'author'}" @click="currentTab = 'author'">Authors</button>
            </li>
        </ul>
            <div v-if="currentTab === 'contributions'"><create-contribution @contributionCreated="fetchContributions" :authors="authors" :books="books" /></div>
            <div v-if="currentTab === 'book'"><create-book @bookCreated="fetchBooks" :authors="authors" /></div>
            <div v-if="currentTab === 'author'"><create-author @authorCreated="fetchAuthors" /></div>
      </div>
    </div>
  </template>
  
  <script>
  import CreateBook from './components/CreateBook.vue';
  import CreateAuthor from './components/CreateAuthor.vue';
  import CreateContribution from './components/CreateContribution.vue';
  
  export default {
    components: {
      CreateBook,
      CreateAuthor,
      CreateContribution
    },
    data() {
      return {
        currentTab: 'contributions',
        authors: [],
        books: [],
        contributions: []
      };
    },
    mounted() {
      this.fetchAuthors();
      this.fetchBooks();
      this.fetchContributions();
    },
    methods: {
      fetchAuthors() {
        fetch('http://localhost:8000/api/authors/')
          .then(response => response.json())
          .then(data => {
            this.authors = data.authors;
          })
          .catch(error => console.error('Error fetching authors:', error));
      },
      fetchBooks() {
        fetch('http://localhost:8000/api/books/')
          .then(response => response.json())
          .then(data => {
            this.books = data.books;
          })
          .catch(error => console.error('Error fetching books:', error));
      },
      fetchContributions() {
        fetch('http://localhost:8000/api/authorbooks/')
          .then(response => response.json())
          .then(data => {
            this.contributions = data.contributions;
          })
          .catch(error => console.error('Error fetching contributions:', error));
      }
    }
  };
  </script>
  