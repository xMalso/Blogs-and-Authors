<template>
    <div>
        <h6>Create New Contribution</h6>
        <form @submit.prevent="submitContribution">
            <div class="mb-2">
                <label for="contributionBook" class="form-label">Select Book</label>
                <select v-model="contribution.book_id" class="form-control" required>
                    <option value="">Select a Book</option>
                    <option v-for="book in books" :key="book.id" :value="book.id">
                        {{ book.title }}
                    </option>
                </select>
            </div>
            <div class="mb-2">
                <label for="contributionAuthor" class="form-label">Select Author</label>
                <select v-model="contribution.author_id" class="form-control" required>
                    <option value="">Select an Author</option>
                    <option v-for="author in authors" :key="author.id" :value="author.id">
                        {{ author.name }}
                    </option>
                </select>
            </div>
            <div class="mb-2">
                <label for="contributionDate" class="form-label">Contribution Date</label>
                <input type="date" v-model="contribution.contribution_date" class="form-control" required />
            </div>
            <div class="mb-2">
                <label for="contributionSummary" class="form-label">Contribution Summary</label>
                <textarea v-model="contribution.contribution_summary" class="form-control" required></textarea>
            </div>
            <div class="mb-2">
                <label for="isPrimaryAuthor" class="form-label">Is Primary Author?</label>
                <select v-model="contribution.is_primary_author" class="form-control" required>
                    <option :value="true">Yes</option>
                    <option :value="false">No</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Create Contribution</button>
        </form>
    </div>
</template>

<script>
export default {
    props: {
        books: Array,
        authors: Array
    },
    data() {
        return {
            contribution: {
                book_id: '',
                author_id: '',
                contribution_date: '',
                contribution_summary: '',
                is_primary_author: false
            }
        };
    },
    methods: {
        submitContribution() {
            if (!this.contribution.book_id || !this.contribution.author_id) {
                alert('Please fill in all fields for the contribution');
                return;
            }
            console.log(this.contribution)
            fetch('http://localhost:8000/api/authorbooks/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.contribution)
            })
                .then(response => response.json().then(data => ({ status: response.status, message: data.message })))
                .then(({ status, message }) => {
                    console.log('Status:', status);
                    console.log('Message:', message);
                    this.$emit('contributionCreated', this.contribution);
                    this.resetForm();
                    alert('Contribution created successfully!');
                })
                .catch(error => {
                    console.error('Error creating contribution:', error);
                    alert('Error creating contribution');
                });
        },
        resetForm() {
            this.contribution = { book_id: '', author_id: '', contribution_date: '', contribution_summary: '', is_primary_author: false };
        }
    }
};
</script>