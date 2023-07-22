<script lang="ts">
	import type { PageData } from './$types';
	import { page } from '$app/stores';
	let params = $page.params.event;
	export let data: PageData;
</script>

<div class="w-full py-4">
	<div>{data.event.name}</div>
	<div>{JSON.stringify(data.parameters)}</div>
</div>
