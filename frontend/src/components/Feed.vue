<template>
    <div class="container">
        <div v-for="feed in feeds"
             :key="feed.header"
             class="feed">
            <a class="img" :href="feed.url2">
                <img :src="feed.image" :alt="feed.alt">
            </a>
            <p>
                <a :href="feed.url1">{{ feed.header }}</a>
            </p>
            <p>{{ feed.additionalInfo }}</p>
        </div>
    </div>
</template>

<script>
export default {
        data: function() {
            return {
                feeds: [
                    { 
                        image: 'imagepath',
                        alt: 'image alt',
                        url1: 'articleurl',
                        url2: 'sourceurl',
                        header: 'feed1 header very long text about some very interesting topic',
                        additionalInfo: 'up: 5000 | down: 1000 | ratio: 0.8'
                    },
                    { 
                        image: 'imagepath',
                        alt: 'image alt',
                        url1: 'articleurl',
                        url2: 'sourceurl',
                        header: 'feed2 header very long text about some very interesting topic',
                        additionalInfo: 'up: 5000 | down: 1000 | ratio: 0.8'
                    },
                    { 
                        image: 'imagepath',
                        alt: 'image alt',
                        url1: 'articleurl',
                        url2: 'sourceurl',
                        header: 'feed3 header very long text about some very interesting topic',
                        additionalInfo: 'up: 5000 | down: 1000 | ratio: 0.8'
                    },
                    { 
                        image: 'imagepath',
                        alt: 'image alt',
                        url1: 'articleurl',
                        url2: 'sourceurl',
                        header: 'feed4 header very long text about some very interesting topic',
                        additionalInfo: 'up: 5000 | down: 1000 | ratio: 0.8'
                    },
                ]
            }
        },
    }
</script>