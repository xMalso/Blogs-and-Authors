<template>
    <div>
        <h5>Create New Book</h5>
        <form @submit.prevent="submitBook">
            <div class="mb-2">
                <label for="bookTitle" class="form-label">Book Title</label>
                <input type="text" id="bookTitle" v-model="book.title" class="form-control" required />
            </div>
            <div class="mb-2">
                <label for="bookDescription" class="form-label">Book Description</label>
                <textarea id="bookDescription" v-model="book.description" class="form-control" required></textarea>
            </div>
            <div class="mb-2">
                <label for="bookFiction" class="form-label">Fiction</label>
                <div><input type="checkbox" id="bookFiction" v-model="book.fiction" class="form-check-input"></div>
            </div>
            <div class="mb-2">
                <label for="author" class="form-label">Select Author</label>
                <select v-model="book.author.author_id" class="form-control" required>
                    <option value="">Select an author</option>
                    <option v-for="author in authors" :key="author.id" :value="author.id">
                        {{ author.name }}
                    </option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Create Book</button>
        </form>
    </div>
</template>

<script>
export default {
    props: ['authors'],
    data() {
        return {
            book: {
                title: '',
                description: '',
                fiction: false,
                author: {
                    author_id: ''
                }
            }
        };
    },
    methods: {
        submitBook() {
            if (!this.book.title || !this.book.description || !this.book.author.author_id) {
                alert('Please fill in all fields for the book');
                return;
            }
            fetch('http://localhost:8000/api/books/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.book)
            })
                .then(response => response.json().then(data => ({ status: response.status, message: data.message, data: data })))
                .then(({ status, message, data }) => {
                    console.log('Status:', status);
                    console.log('Message:', message);
                    console.log(data)
                    this.book['id'] = data.id
                    this.book['publish_date'] = data.publish_date
                    this.$emit('bookCreated',this.book)
                    console.log(this.book)
                    this.resetForm();
                    alert('Book created successfully!');
                })
                .catch(error => {
                    console.error('Error creating book:', error);
                    alert('Error creating book');
                });
        },
        resetForm() {
            this.book = {
                title: '',
                description: '',
                fiction: false,
                author: {
                    author_id: ''
                }
            };
        }
    }
};
</script>