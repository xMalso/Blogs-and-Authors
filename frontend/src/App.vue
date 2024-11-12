<template>
    <div class="container pt-3">
        <div class="pb-3">
            <createBook></createBook>
        </div>
    </div>
</template>

<script>
import createBook from './components/create_book.vue';

export default {
    components: {
        createBook, // Register the component here
    },
    data() {
        return {
            response_data: '',
        }
    },
    async mounted() {
       
    },
    methods: {}
}
</script>