<template>
    <div class="container pt-3">
        <div class="pb-3">
            <!-- Pills Navigation -->
            <ul class="nav nav-pills">
                <li class="nav-item">
                    <button class="nav-link" :class="{ active: currentTab === 'contributions' }"
                        @click="currentTab = 'contributions'">Contributions</button>
                </li>
                <li class="nav-item">
                    <button class="nav-link" :class="{ active: currentTab === 'book' }"
                        @click="currentTab = 'book'">Books</button>
                </li>
                <li class="nav-item">
                    <button class="nav-link" :class="{ active: currentTab === 'author' }"
                        @click="currentTab = 'author'">Authors</button>
                </li>
            </ul>

            <!-- Content Sections -->
            <div v-if="currentTab === 'contributions'">
                <button class="btn btn-success mt-3" @click="showModal('contributionModal')">Create Contribution</button>
                <ul class="list-group mt-3">
                    <li v-for="contribution in contributions" :key="contribution.id" class="list-group-item">
                        <strong>{{ contribution.contribution_summary }}</strong> by {{ authorMap[contribution.author_id] }} for {{ bookMap[contribution.book_id] }} at {{ contribution.contribution_date }}
                        <button class="btn btn-warning btn-sm float-end ms-2" @click="editContribution(contribution)">Edit</button>
                        <button class="btn btn-danger btn-sm float-end" @click="deleteContribution(contribution.id)">Delete</button>
                    </li>
                </ul>
            </div>

            <div v-if="currentTab === 'book'">
                <button class="btn btn-success mt-3" @click="showModal('bookModal')">Create Book</button>
                <ul class="list-group mt-3">
                    <li v-for="book in books" :key="book.id" class="list-group-item">
                        <strong>{{ book.title }}</strong> - {{ book.description }} at {{  book.publish_date }}
                        <button class="btn btn-warning btn-sm float-end ms-2" @click="editBook(book)">Edit</button>
                        <button class="btn btn-danger btn-sm float-end" @click="deleteBook(book.id)">Delete</button>
                    </li>
                </ul>
            </div>

            <div v-if="currentTab === 'author'">
                <button class="btn btn-success mt-3" @click="showModal('authorModal')">Create Author</button>
                <ul class="list-group mt-3">
                    <li v-for="author in authors" :key="author.id" class="list-group-item">
                        <strong>{{ author.name }}</strong> - {{ author.bio }}
                        <button class="btn btn-warning btn-sm float-end ms-2" @click="editAuthor(author)">Edit</button>
                        <button class="btn btn-danger btn-sm float-end" @click="deleteAuthor(author.id)">Delete</button>
                    </li>
                </ul>
            </div>

            <!-- Modals -->
            <div class="modal fade" id="contributionModal" tabindex="-1">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">{{ contributionToEdit ? 'Edit Contribution' : 'Create Contribution' }}</h5>
                            <button type="button" class="btn-close" @click="hideModal('contributionModal')"></button>
                        </div>
                        <div class="modal-body">
                            <create-contribution v-if="contributionToEdit" :authors="authors" :books="books"
                                :contributionToEdit="contributionToEdit"
                                @contributionUpdated="handleContributionUpdated" />
                            <create-contribution v-else :authors="authors" :books="books"
                                @contributionCreated="handleContributionCreated" />
                        </div>
                    </div>
                </div>
            </div>

            <div class="modal fade" id="bookModal" tabindex="-1">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">{{ bookToEdit ? 'Edit Book' : 'Create Book' }}</h5>
                            <button type="button" class="btn-close" @click="hideModal('bookModal')"></button>
                        </div>
                        <div class="modal-body">
                            <create-book v-if="bookToEdit" :book="bookToEdit" @bookUpdated="handleBookUpdated" />
                            <create-book v-else @bookCreated="fetchBooks; hideModal('bookModal')" :authors="authors" />
                        </div>
                    </div>
                </div>
            </div>

            <div class="modal fade" id="authorModal" tabindex="-1">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">{{ authorToEdit ? 'Edit Author' : 'Create Author' }}</h5>
                            <button type="button" class="btn-close" @click="hideModal('authorModal')"></button>
                        </div>
                        <div class="modal-body">
                            <create-author v-if="authorToEdit" :author="authorToEdit" @authorUpdated="handleAuthorUpdated" />
                            <create-author v-else @authorCreated="addAuthor; hideModal('authorModal')" />
                        </div>
                    </div>
                </div>
            </div>
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
            contributions: [],
            contributionToEdit: null,
            authorToEdit: null,
            bookToEdit: null
        };
    },
    computed: {
        authorMap() {
            return this.authors.reduce((map, author) => {
                map[author.id] = author.name;
                return map;
            }, {});
        },
        bookMap() {
            return this.books.reduce((map, book) => {
                map[book.id] = book.title;
                return map;
            }, {});
        }
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
                    this.contributions = data.cont;
                })
                .catch(error => console.error('Error fetching contributions:', error));
        },
        addContribution(newContribution) {
            this.contributions.push(newContribution);
        },
        updateContribution(updatedContribution) {
            const index = this.contributions.findIndex(c => c.id === updatedContribution.id);
            if (index !== -1) {
                this.contributions[index] = updatedContribution;
            }
        },
        addAuthor(newAuthor) {
            this.authors.push(newAuthor);
        },
        addBook(newBook) {
            this.books.push(newBook);
        },
        showModal(modalId) {
            const modalElement = document.getElementById(modalId);
            const modal = new bootstrap.Modal(modalElement);
            modal.show();
        },
        hideModal(modalId) {
            const modalElement = document.getElementById(modalId);
            const modal = bootstrap.Modal.getInstance(modalElement);
            modal.hide();
        },
        deleteContribution(contributionId) {
            fetch(`http://localhost:8000/api/authorbooks/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id: contributionId })
            })
                .then(response => {
                    if (response.status === 204) {
                        this.contributions = this.contributions.filter(contribution => contribution.id !== contributionId);
                        alert('Contribution deleted successfully!');
                    } else {
                        return response.json().then(data => {
                            alert('Error deleting contribution: ' + data.message);
                        });
                    }
                })
                .catch(error => alert('Error deleting contribution'));
        },

        deleteBook(bookId) {
            fetch(`http://localhost:8000/api/books/`, {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({id:bookId})
            })
                .then(response => {
                    if (response.status === 204) {
                        this.books = this.books.filter(book => book.id !== bookId);
                        alert('Book deleted successfully!');
                    } else {
                        return response.json().then(data => alert('Error deleting book: ' + data.message));
                    }
                })
                .catch(error => alert('Error deleting book'));
        },

        deleteAuthor(authorId) {
            fetch(`http://localhost:8000/api/authors/`, {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({id:authorId})
            })
                .then(response => {
                    if (response.status === 204) {
                        this.authors = this.authors.filter(author => author.id !== authorId);
                        alert('Author deleted successfully!');
                    } else {
                        return response.json().then(data => alert('Error deleting author: ' + data.message));
                    }
                })
                .catch(error => alert('Error deleting author'));
        },

        editContribution(contribution) {
            this.contributionToEdit = { ...contribution };
            this.showModal('contributionModal');
        },

        editBook(book) {
            this.bookToEdit = { ...book };
            this.showModal('bookModal');
        },

        editAuthor(author) {
            this.authorToEdit = { ...author };
            this.showModal('authorModal');
        },

        handleContributionUpdated(updatedContribution) {
            this.updateContribution(updatedContribution);
            this.hideModal('contributionModal');
        },

        handleContributionCreated(newContribution) {
            this.addContribution(newContribution);
            this.hideModal('contributionModal');
        },

        handleBookUpdated(updatedBook) {
            const index = this.books.findIndex(b => b.id === updatedBook.id);
            if (index !== -1) {
                this.books[index] = updatedBook;
            }
            this.hideModal('bookModal');
        },

        handleAuthorUpdated(updatedAuthor) {
            const index = this.authors.findIndex(a => a.id === updatedAuthor.id);
            if (index !== -1) {
                this.authors[index] = updatedAuthor;
            }
            this.hideModal('authorModal');
        }
    }
};
</script>