<script lang="ts">
	import '../app.css';
	import { page } from '$app/stores';
	// @ts-ignore
	import Footer from '$lib/footer.svelte';
	// @ts-ignore
	import Header from '$lib/header.svelte';
	// @ts-ignore
	import HeaderCore from '$lib/header-core.svelte';

	function isCoreArea(path: String) {
		return path.startsWith('/events') ||
			path.startsWith('/parameters') ||
			path.startsWith('/triggers')
			? true
			: false;
	}
</script>

{#if isCoreArea($page.url.pathname)}
	<HeaderCore />
{:else}
	<Header />
{/if}

<slot />

<Footer />
