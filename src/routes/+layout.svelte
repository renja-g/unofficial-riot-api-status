<script>
	import './styles.css';
	import Header from '../lib/components/Header/Header.svelte';
	import SideBar from '../lib/components/SideBar/SideBar.svelte';
	import Canvas from '../lib/components/Canvas/Canvas.svelte';
</script>

<div class="app">
	<Header />

	<main>
		<SideBar />
		<slot />
	</main>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		height: 100vh;
	}

	main {
		display: flex;
		flex: 1;
	}
</style>
