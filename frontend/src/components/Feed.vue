<template>
    <div class="container">
        <div v-for="feed in feedsData" :key="feed.header" class="feed">
            <a class="image-container" :href="feed.url2">
                <img class="img" :src="feed.image" :alt="feed.alt" />
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
import { mapActions } from 'vuex';
import reddit_logo from '../media/reddit_logo.jpeg';

export default {
    props: ['category', 'categoryKey'],
    data() {
        return {
            feedsData: undefined,
        };
    },
    methods: {
        ...mapActions({
            getFeeds(dispatch) {
                dispatch('feed/getFeeds', { category: this.category, key: this.categoryKey }).then(
                    (data) => {
                        switch (this.category) {
                            case 'reddit':
                                this.feedsData = data.map((i) => {
                                    return {
                                        header: i.title,
                                        url1: i.link_url,
                                        url2: i.reddit_url,
                                        additionalInfo: i.rating,
                                        image: i.image != null ? i.image : reddit_logo,
                                    };
                                });
                                break;
                            case 'newsapi':
                                this.feedsData = data.map((i) => {
                                    return {
                                        header: i.title,
                                        url1: i.url,
                                        url2: i.url,
                                        additionalInfo: i.time_published,
                                        image: i.image,
                                    };
                                });
                                break;
                        }
                    }
                );
            },
        }),
    },
    created() {
        const data = this.getFeeds();
        this.feedsData = this.mapLocalFeeds(data);
    },
};
</script>
