<template>
    <header>
        <h1 class="title">Header here</h1>
        <ul class="menu">
            <li class="item" v-for="item in menuItems" :key="item.link">
                <a :href="'#' + item.link">
                    {{ item.text }}
                </a>
            </li>
        </ul>
    </header>
</template>

<script>
export default {
    data() {
        return {
            menuItems: [
                { text: 'item1', link: 'block1' },
                { text: 'item2', link: 'block2' },
                { text: 'item3', link: 'block3' },
            ],
        };
    },
};
</script>
