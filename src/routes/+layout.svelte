<script>
	import './styles.css';
	import Header from '../lib/components/Header/Header.svelte';
</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

	<!-- Footer -->
</div>

<style>
/* Center app */
.app {
	display: flex;
	flex-direction: column;
	min-height: 100vh;
}

/* Center main */
main {
	flex: 1;
	display: flex;
	flex-direction: column;
	align-items: center;
}

</style>
