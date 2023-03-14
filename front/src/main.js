const App = {
    data() {
        return {
            tasks: ['test'],
        }
    },
    compilerOptions: {
        delimiters: ['[[', ']]'],
    },
    methods: {
    },
    created() {
    },
}

Vue.createApp(App).mount('#app')