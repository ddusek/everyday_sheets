<template>
    <div class="container">
        <div id="block1" class="feed-block">
            <div class="feed-header">
                <h2>Reddit</h2>
            </div>
            <Feed category="reddit" />
        </div>
        <div id="block2" class="feed-block">
            <div class="feed-header">
                <h2>CZ</h2>
            </div>
            <Feed category="newsapi" categoryKey="cz" />
        </div>
        <div id="block3" class="feed-block">
            <div class="feed-header">
                <h2>General</h2>
            </div>
            <Feed category="newsapi" categoryKey="general" />
        </div>
        <div id="block4" class="feed-block">
            <div class="feed-header">
                <h2>Technology</h2>
            </div>
            <Feed category="newsapi" categoryKey="technology" />
        </div>
        <div id="block5" class="feed-block">
            <div class="feed-header">
                <h2>Science</h2>
            </div>
            <Feed category="newsapi" categoryKey="science" />
        </div>
        <div id="block5" class="feed-block">
            <div class="feed-header">
                <h2>Gaming</h2>
            </div>
            <Feed category="newsapi" categoryKey="gaming" />
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
