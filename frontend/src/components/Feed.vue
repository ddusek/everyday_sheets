<template>
    <div class="container">
        <button @click="refreshData">refresh</button>
        <div v-for="feed in computedItems" :key="feed.header" class="feed">
            <a class="img" :href="feed.url2">
                <img :src="feed.image" :alt="feed.alt" />
            </a>
            <div class="content">
                <p>
                    <a :href="feed.url1">{{ feed.header }}</a>
                </p>
                <p>{{ feed.additionalInfo }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    computed: mapGetters({
        computedItems: 'feed/redditFeeds',
    }),
    methods: {
        ...mapActions({
            getNews: 'feed/getNewsAsync',
        }),
        refreshData() {
            this.getNews();
        },
    },
    created() {
        this.getNews();
    },
};
</script>
