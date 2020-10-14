<template>
    <div class="container">
        <div id="block1" class="feed-block">
            <div class="feed-header">
                <h2>FeedHeader</h2>
            </div>
            <Feed />
        </div>
        <div id="block2" class="feed-block">
            <div class="feed-header">
                <h2>FeedHeader</h2>
            </div>
            <Feed />
        </div>
        <div id="block3" class="feed-block">
            <div class="feed-header">
                <h2>FeedHeader</h2>
            </div>
            <Feed />
        </div>
    </div>
</template>

<script>
import Feed from './Feed';
export default {
    components: {
        Feed,
    },
};
</script>
