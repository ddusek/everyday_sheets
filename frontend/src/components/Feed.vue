<template>
    <div class="container">
        <button @click="getData">iksde</button>
        <div v-for="feed in feeds" :key="feed.header" class="feed">
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
export default {
    data() {
        return {
            feeds: [
                {
                    image: 'imagepath',
                    alt: 'image alt',
                    url1: 'articleurl',
                    url2: 'sourceurl',
                    header: 'feed1 header very long text about some very interesting topic',
                    additionalInfo: 'up: 5000 | down: 1000 | ratio: 0.8',
                },
                {
                    image: 'imagepath',
                    alt: 'image alt',
                    url1: 'articleurl',
                    url2: 'sourceurl',
                    header: 'feed2 header very long text about some very interesting topic',
                    additionalInfo: 'up: 5000 | down: 1000 | ratio: 0.8',
                },
                {
                    image: 'imagepath',
                    alt: 'image alt',
                    url1: 'articleurl',
                    url2: 'sourceurl',
                    header: 'feed3 header very long text about some very interesting topic',
                    additionalInfo: 'up: 5000 | down: 1000 | ratio: 0.8',
                },
                {
                    image: 'imagepath',
                    alt: 'image alt',
                    url1: 'articleurl',
                    url2: 'sourceurl',
                    header: 'feed4 header very long text about some very interesting topic',
                    additionalInfo: 'up: 5000 | down: 1000 | ratio: 0.8',
                },
                // {
                //     header: this.$store.state.feeds.title,
                //     additionalInfo: this.$store.state.feeds.rating,
                //     url1: this.$store.state.feeds.reddit_url,
                //     url2: this.$store.state.feeds.link_url,
                // },
            ],
        };
    },
    methods: {
        getData() {
            this.$store.dispatch('feed/getNews');
            console.log(this.$store.state.feeds);
        },
    },
};
</script>
