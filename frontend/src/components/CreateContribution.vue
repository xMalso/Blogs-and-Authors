<template>
    <div>
        <h6>{{ contribution.id ? 'Edit Contribution' : 'Create New Contribution' }}</h6>
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
            <button type="submit" class="btn btn-primary">
                {{ contribution.id ? 'Update Contribution' : 'Create Contribution' }}
            </button>
        </form>
    </div>
</template>

<script>
export default {
    props: {
        books: Array,
        authors: Array,
        contributionToEdit: Object
    },
    data() {
        return {
            contribution: {
                book_id: '',
                author_id: '',
                contribution_summary: '',
                is_primary_author: false,
                id: null
            }
        };
    },
    watch: {
        contributionToEdit: {
            immediate: true,
            handler(newVal) {
                if (newVal && newVal.id) {
                    this.contribution = { ...newVal };
                }
            }
        }
    },
    methods: {
        submitContribution() {
            if (!this.contribution.book_id || !this.contribution.author_id) {
                alert('Please fill in all fields for the contribution');
                return;
            }
            if (this.contribution.id) {
                this.updateContribution();
            } else {
                this.createContribution();
            }
        },
        createContribution() {
            fetch('http://localhost:8000/api/authorbooks/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.contribution)
            })
                .then(response => response.json())
                .then(data => {
                    this.contribution.id = data.id
                    this.contribution.contribution_date = data.date
                    this.$emit('contributionCreated', this.contribution);
                    this.resetForm();
                    alert('Contribution created successfully!');
                })
                .catch(error => {
                    console.error('Error creating contribution:', error);
                    alert('Error creating contribution');
                });
        },
        updateContribution() {
            fetch(`http://localhost:8000/api/authorbooks/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.contribution)
            })
                .then(response => response.json())
                .then(data => {
                    this.$emit('contributionUpdated', this.contribution);
                    this.resetForm();
                    alert('Contribution updated successfully!');
                })
                .catch(error => {
                    console.error('Error updating contribution:', error);
                    alert('Error updating contribution');
                });
        },
        deleteContribution() {
            fetch(`http://localhost:8000/api/authorbooks/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id: this.contribution.id })
            })
                .then(response => {
                    if (response.ok) {
                        this.$emit('contributionDeleted', this.contribution.id);
                        this.resetForm();
                        alert('Contribution deleted successfully!');
                    } else {
                        response.json().then(data => {
                            console.error('Error deleting contribution:', data);
                            alert('Error deleting contribution');
                        });
                    }
                })
                .catch(error => {
                    console.error('Error deleting contribution:', error);
                    alert('Error deleting contribution');
                });
        },
        resetForm() {
            this.contribution = { book_id: '', author_id: '', contribution_summary: '', is_primary_author: false, id: null };
        }
    }
};
</script>