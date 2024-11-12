<template>
  <div class="container">
    <!-- Tabs Navigation -->
    <ul class="nav nav-tabs" id="bookTabs" role="tablist">
      <li class="nav-item" role="presentation">
        <a class="nav-link active" id="book-tab" data-bs-toggle="tab" href="#book" role="tab" aria-controls="book" aria-selected="true">Books</a>
      </li>
      <li class="nav-item" role="presentation">
        <a class="nav-link" id="author-tab" data-bs-toggle="tab" href="#author" role="tab" aria-controls="author" aria-selected="false">Authors</a>
      </li>
      <li class="nav-item" role="presentation">
        <a class="nav-link" id="contribution-tab" data-bs-toggle="tab" href="#contribution" role="tab" aria-controls="contribution" aria-selected="false">Contributions</a>
      </li>
    </ul>

    <!-- Tab Content -->
    <div class="tab-content mt-3">
      <!-- Books Tab -->
      <div class="tab-pane fade show active" id="book" role="tabpanel" aria-labelledby="book-tab">
        <div class="mb-3">
          <h5>Create New Book</h5>
          <form @submit.prevent="createBook">
            <div class="mb-2">
              <label for="bookTitle" class="form-label">Book Title</label>
              <input type="text" id="bookTitle" v-model="newBook.title" class="form-control" required />
            </div>
            <div class="mb-2">
              <label for="bookDescription" class="form-label">Book Description</label>
              <textarea id="bookDescription" v-model="newBook.description" class="form-control" required></textarea>
            </div>

            <!-- Author Selection -->
            <div class="mb-2">
              <label for="authors" class="form-label">Select Authors</label>
              <div v-for="(slot, index) in authorSlots" :key="index" class="mb-2">
                <select v-model="newBook.authors[index].author_id" class="form-control" required>
                  <option value="">Select an author</option>
                  <option v-for="author in authors" :key="author.id" :value="author.id">
                    {{ author.name }}
                  </option>
                </select>

                <!-- Remove Author Field -->
                <button v-if="authorSlots.length > 1" @click="removeAuthorField(index)" class="btn btn-danger btn-sm mt-2">Remove</button>
              </div>

              <!-- Add Another Author -->
              <button v-if="authorSlots.length < 3" @click="addAuthorField" class="btn btn-primary mt-2">Add Another Author</button>
            </div>

            <!-- Submit Button -->
            <button type="submit" class="btn btn-primary">Create Book</button>
          </form>
        </div>

    <!-- Books List Section -->
<h5>Books List</h5>
<ul class="list-group">
  <li v-for="book in books" :key="book.id" class="list-group-item">
    <div>
      <strong>Title:</strong> {{ book.title }}
    </div>
    <div>
      <strong>Description:</strong> {{ book.description }}
    </div>
    <!-- Display Authors -->
    <div>
      <strong>Authors:</strong>
      <span v-for="(author, index) in book.authors" :key="index">{{ author.name }}<span v-if="index < book.authors.length - 1">, </span></span>
    </div>

    <!-- Edit Book Button -->
    <button @click="editBook(book.id)" class="btn btn-warning btn-sm mt-2">Edit Book</button>

    <!-- Delete Book Button -->
    <button @click="deleteBook(book.id)" class="btn btn-danger btn-sm mt-2">Delete Book</button>
  </li>
</ul>
      </div>

      <!-- Authors Tab -->
      <div class="tab-pane fade" id="author" role="tabpanel" aria-labelledby="author-tab">
        <!-- Create New Author Form -->
        <div class="mb-3">
          <h5>Create New Author</h5>
          <form @submit.prevent="createAuthor">
            <div class="mb-2">
              <label for="authorName" class="form-label">Author Name</label>
              <input type="text" id="authorName" v-model="newAuthor.name" class="form-control" required />
            </div>
            <div class="mb-2">
              <label for="authorBio" class="form-label">Author Bio</label>
              <textarea id="authorBio" v-model="newAuthor.bio" class="form-control" required></textarea>
            </div>
            <div class="mb-2">
              <label for="authorAge" class="form-label">Author Age</label>
              <input type="number" id="authorAge" v-model="newAuthor.age" class="form-control" required />
            </div>
            <button type="submit" class="btn btn-primary">Create Author</button>
          </form>
        </div>

        <!-- Authors List Section -->
        <h5>Authors List</h5>
        <ul class="list-group">
          <li v-for="author in authors" :key="author.id" class="list-group-item">
            <div>
              <strong>Name:</strong> {{ author.name }}
            </div>
            <div>
              <strong>Bio:</strong> {{ author.bio }}
            </div>
            <div>
              <strong>Age:</strong> {{ author.age }}
            </div>
            <button @click="deleteAuthor(author.id)" class="btn btn-danger btn-sm">Delete</button>
          </li>
        </ul>
      </div>

      <!-- Contributions Tab -->
      <div class="tab-pane fade" id="contribution" role="tabpanel" aria-labelledby="contribution-tab">
        <h5>Book Contributions</h5>

        <!-- Contribution Form -->
        <div class="mb-3">
          <h6>Create New Contribution</h6>
          <form @submit.prevent="createContribution">
            <div class="mb-2">
              <label for="contributionBook" class="form-label">Select Book</label>
              <select v-model="newContribution.book_id" class="form-control" required>
                <option value="">Select a Book</option>
                <option v-for="book in books" :key="book.id" :value="book.id">
                  {{ book.title }}
                </option>
              </select>
            </div>
            <div class="mb-2">
              <label for="contributionAuthor" class="form-label">Select Author</label>
              <select v-model="newContribution.author_id" class="form-control" required>
                <option value="">Select an Author</option>
                <option v-for="author in authors" :key="author.id" :value="author.id">
                  {{ author.name }}
                </option>
              </select>
            </div>
            <div class="mb-2">
              <label for="contributionDate" class="form-label">Contribution Date</label>
              <input type="date" v-model="newContribution.contribution_date" class="form-control" required />
            </div>
            <div class="mb-2">
              <label for="contributionSummary" class="form-label">Contribution Summary</label>
              <textarea v-model="newContribution.contribution_summary" class="form-control" required></textarea>
            </div>
            <div class="mb-2">
              <label for="isPrimaryAuthor" class="form-label">Is Primary Author?</label>
              <select v-model="newContribution.is_primary_author" class="form-control" required>
                <option :value="true">Yes</option>
                <option :value="false">No</option>
              </select>
            </div>
            <button type="submit" class="btn btn-primary">Create Contribution</button>
          </form>
        </div>

        <!-- Contributions List Section -->
        <div v-if="contributions.length > 0">
          <h6>Contributions List</h6>
          <ul class="list-group">
            <li v-for="contribution in contributions" :key="contribution.id" class="list-group-item">
              <strong>{{ contribution.author_name }}</strong> - {{ contribution.book_title }}
              <p>{{ contribution.contribution_type }} (Primary: {{ contribution.is_primary_author ? 'Yes' : 'No' }})</p>
              <p><small>Contributed on: {{ formatDate(contribution.contribution_date) }}</small></p>
              <p><small>Summary: {{ contribution.contribution_summary }}</small></p>
            </li>
          </ul>
        </div>
        <div v-else>
          <p>No contributions available.</p>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      authors: [],
      books: [],
      contributions: [],
      newBook: {
        title: '',
        description: '',
        authors: [{ author_id: '', contribution_date: '', contribution_summary: '' }]
      },
      newAuthor: {
        name: '',
        bio: '',
        age: null
      },
      authorSlots: [0], // Track the number of author fields (up to 3)
      currentBookId: null,
      newContribution: {
        book_id: '',
        author_id: '',
        contribution_date: '',
        contribution_summary: '',
        is_primary_author: false
      }
    };
  },
  mounted() {
    this.fetchAuthors();
    this.fetchBooks();
    this.fetchContributions();
  },
  methods: {
    // Fetch authors data
    fetchAuthors() {
      fetch('http://localhost:8000/api/authors/')
        .then(response => response.json())
        .then(data => {
          this.authors = data;
        })
        .catch(error => console.error('Error fetching authors:', error));
    },

    // Fetch books data
    fetchBooks() {
      fetch('http://localhost:8000/api/books/')
        .then(response => response.json())
        .then(data => {
          this.books = data;
        })
        .catch(error => console.error('Error fetching books:', error));
    },

    // Fetch contributions data
    fetchContributions() {
      fetch('http://localhost:8000/api/contributions/')
        .then(response => response.json())
        .then(data => {
          this.contributions = data;
        })
        .catch(error => console.error('Error fetching contributions:', error));
    },

    // Create a new book
    createBook() {
      if (!this.newBook.title || !this.newBook.description) {
        alert('Please fill in all fields for the book');
        return;
      }

      const bookData = {
        title: this.newBook.title,
        description: this.newBook.description,
        authors: this.newBook.authors.map(author => ({
          author_id: author.author_id,
          contribution_date: author.contribution_date,
          contribution_summary: author.contribution_summary
        }))
      };

      fetch('http://localhost:8000/api/books/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(bookData)
      })
        .then(response => response.json())
        .then(data => {
          if (data) {
            this.books.push(data);
            this.resetForm();
            alert('Book created successfully!');
          }
        })
        .catch(error => {
          console.error('Error creating book:', error);
          alert('Error creating book');
        });
    },

    // Create a new author
    createAuthor() {
      if (!this.newAuthor.name || !this.newAuthor.bio || !this.newAuthor.age) {
        alert('Please fill in all fields for the author');
        return;
      }

      const authorData = {
        name: this.newAuthor.name,
        bio: this.newAuthor.bio,
        age: this.newAuthor.age
      };

      fetch('http://localhost:8000/api/authors/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(authorData)
      })
        .then(response => response.json())
        .then(data => {
          if (data) {
            this.authors.push(data);
            this.resetAuthorForm();
            alert('Author created successfully!');
          }
        })
        .catch(error => {
          console.error('Error creating author:', error);
          alert('Error creating author');
        });
    },

    // Create a new contribution (AuthorBook)
    createContribution() {
      if (!this.newContribution.book_id || !this.newContribution.author_id) {
        alert('Please fill in all fields for the contribution');
        return;
      }

      const contributionData = {
        book_id: this.newContribution.book_id,
        author_id: this.newContribution.author_id,
        contribution_date: this.newContribution.contribution_date,
        contribution_summary: this.newContribution.contribution_summary,
        is_primary_author: this.newContribution.is_primary_author
      };

      fetch('http://localhost:8000/api/contributions/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(contributionData)
      })
        .then(response => response.json())
        .then(data => {
          this.contributions.push(data);
          this.resetContributionForm();
          alert('Contribution created successfully!');
        })
        .catch(error => {
          console.error('Error creating contribution:', error);
          alert('Error creating contribution');
        });
    },

    // Add a new author field for a book
    addAuthorField() {
      if (this.authorSlots.length < 3) {
        this.authorSlots.push(this.authorSlots.length);
        this.newBook.authors.push({
          author_id: '',
          contribution_date: '',
          contribution_summary: ''
        });
      } else {
        alert('You can only add up to 3 authors for a book');
      }
    },

    // Remove an author field for a book
    removeAuthorField(index) {
      if (this.authorSlots.length > 1) {
        this.authorSlots.splice(index, 1);
        this.newBook.authors.splice(index, 1);
      }
    },

    // Edit an existing book
    editBook(bookId) {
      const bookToEdit = this.books.find(book => book.id === bookId);
      if (bookToEdit) {
        this.newBook = {
          title: bookToEdit.title,
          description: bookToEdit.description,
          authors: bookToEdit.authors.map(author => ({
            author_id: author.author_id,
            contribution_date: author.contribution_date,
            contribution_summary: author.contribution_summary
          }))
        };
        this.currentBookId = bookId;
      }
    },

    // Update an existing book
    updateBook() {
      if (!this.currentBookId) {
        console.error('No book selected for updating');
        return;
      }

      const updatedBookData = {
        title: this.newBook.title,
        description: this.newBook.description,
        authors: this.newBook.authors,
        id: this.currentBookId
      };

      fetch(`http://localhost:8000/api/books/${this.currentBookId}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedBookData)
      })
        .then(response => response.json())
        .then(data => {
          const bookIndex = this.books.findIndex(b => b.id === this.currentBookId);
          if (bookIndex !== -1) {
            this.books.splice(bookIndex, 1, data);
          }
          this.resetForm();
          alert('Book updated successfully!');
        })
        .catch(error => {
          console.error('Error updating book:', error);
          alert('Error updating book');
        });
    },

    // Delete an existing book
    deleteBook(bookId) {
      fetch(`http://localhost:8000/api/books/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: bookId })
      })
        .then(response => {
          if (response.ok) {
            this.books = this.books.filter(book => book.id !== bookId);
            alert('Book deleted successfully');
          } else {
            alert('Error deleting book');
          }
        })
        .catch(error => console.error('Error deleting book:', error));
    },

    // Delete an author
    deleteAuthor(authorId) {
      fetch(`http://localhost:8000/api/authors/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: authorId })
      })
        .then(response => {
          if (response.ok) {
            this.authors = this.authors.filter(author => author.id !== authorId);
            alert('Author deleted successfully');
          } else {
            alert('Error deleting author');
          }
        })
        .catch(error => console.error('Error deleting author:', error));
    },

    // Reset book form after submission
    resetForm() {
      this.newBook = {
        title: '',
        description: '',
        authors: [{ author_id: '', contribution_date: '', contribution_summary: '' }]
      };
      this.currentBookId = null;
    },

    // Reset author form after submission
    resetAuthorForm() {
      this.newAuthor = {
        name: '',
        bio: '',
        age: null
      };
    },

    // Reset contribution form after submission
    resetContributionForm() {
      this.newContribution = {
        book_id: '',
        author_id: '',
        contribution_date: '',
        contribution_summary: '',
        is_primary_author: false
      };
    },

    // Format date for displaying
    formatDate(date) {
      const d = new Date(date);
      return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
    }
  }
};
</script>