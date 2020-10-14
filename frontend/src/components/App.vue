<template>
    <div id="app">
        <Header />
        <div id="main">
            <FeedBlock />
        </div>
    </div>
</template>

<script>
import Header from './Header.vue';
import FeedBlock from './FeedBlock.vue';
export default {
    components: {
        Header,
        FeedBlock,
    },
};
</script>
