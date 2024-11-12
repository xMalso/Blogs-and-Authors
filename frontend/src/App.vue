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
                <button class="btn btn-primary mt-3" @click="showModal('contributionModal')">Create
                    Contribution</button>
                <ul class="list-group mt-3">
                    <li v-for="contribution in contributions" :key="contribution.id" class="list-group-item">
                        <strong>{{ contribution.contribution_summary }}</strong> by {{ contribution.author_name }} for
                        {{ contribution.book_title }}
                    </li>
                </ul>
            </div>
            <div v-if="currentTab === 'book'">
                <button class="btn btn-primary mt-3" @click="showModal('bookModal')">Create Book</button>
                <ul class="list-group mt-3">
                    <li v-for="book in books" :key="book.id" class="list-group-item">
                        <strong>{{ book.title }}</strong> - {{ book.description }}
                    </li>
                </ul>
            </div>
            <div v-if="currentTab === 'author'">
                <button class="btn btn-primary mt-3" @click="showModal('authorModal')">Create Author</button>
                <ul class="list-group mt-3">
                    <li v-for="author in authors" :key="author.id" class="list-group-item">
                        <strong>{{ author.name }}</strong> - {{ author.bio }}
                    </li>
                </ul>
            </div>

            <!-- Modals -->
            <div class="modal fade" id="contributionModal" tabindex="-1">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Create Contribution</h5>
                            <button type="button" class="btn-close" @click="hideModal('contributionModal')"></button>
                        </div>
                        <div class="modal-body">
                            <create-contribution
                                @contributionCreated="fetchContributions; hideModal('contributionModal')"
                                :authors="authors" :books="books" />
                        </div>
                    </div>
                </div>
            </div>

            <div class="modal fade" id="bookModal" tabindex="-1">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Create Book</h5>
                            <button type="button" class="btn-close" @click="hideModal('bookModal')"></button>
                        </div>
                        <div class="modal-body">
                            <create-book @bookCreated="fetchBooks; hideModal('bookModal')" :authors="authors" />
                        </div>
                    </div>
                </div>
            </div>

            <div class="modal fade" id="authorModal" tabindex="-1">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Create Author</h5>
                            <button type="button" class="btn-close" @click="hideModal('authorModal')"></button>
                        </div>
                        <div class="modal-body">
                            <create-author @authorCreated="addAuthor; hideModal('authorModal')" />
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
            console.log('error')
            fetch('http://localhost:8000/api/authorbooks/')
                .then(response => response.json())
                .then(data => {
                    this.contributions = data.cont;
                })
                .catch(error => console.error('Error fetching contributions:', error));
        },
        addAuthor(newAuthor) {
            this.authors.push(newAuthor);
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
        }
    }
};
</script>