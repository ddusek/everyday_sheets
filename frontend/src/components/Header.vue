<template>
    <div class="header">
        <h1 class="title">Header here</h1>
        <ul class=menu>
            <li class=item
                v-for="item in menuItems"
                :key="item.text">
                <a :href="'#'+item.text">
                    {{ item.text }}
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            menuItems: [
                { text: 'item1' },
                { text: 'item2' },
                { text: 'item3' }
            ]
        }
    }
}
</script>