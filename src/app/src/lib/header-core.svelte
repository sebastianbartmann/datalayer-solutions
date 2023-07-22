<script lang="ts">
	import { onMount } from 'svelte';
	import { themeChange } from 'theme-change';

	// NOTE: the element that is using one of the theme attributes must be in the DOM on mount
	onMount(() => {
		themeChange(false);
		// 👆 false parameter is required for svelte
	});
</script>

<nav>
	<div
		class="
	sticky top-0 z-30 flex h-16 w-full justify-center backdrop-blur transition-all duration-100
	 text-base-content shadow-sm
	"
	>
		<div class="navbar w-full">
			<div class="navbar-start">
				<div class="flex m-8">
					<div class="flex-auto m-2">
						<a href="/events" class="px-2 py-1 underline rounded">Events</a>
					</div>
					<div class="flex-auto m-2">
						<a href="/parameters" class="px-2 py-1 underline rounded">Parameters</a>
					</div>
					<div class="flex-auto m-2">
						<a href="/triggers" class="px-2 py-1 underline rounded">Triggers</a>
					</div>
				</div>
			</div>
			<div class="navbar-center">
				<a href="https://datalayer.solutions" class="normal-case text-xl">datalayer solutions</a>
			</div>
			<div class="navbar-end">
				<div class="items-center flex m-2">
					<span class="m-2">darkmode:</span>
					<input
						data-act-class="ACTIVECLASS"
						data-toggle-theme="light,dark"
						type="checkbox"
						class="toggle toggle-sm"
						checked
					/>
				</div>
				<a
					href="https://github.com/sebastianbartmann/datalayer-solutions"
					class="mr-2 w-8 h-8 btn btn-ghost btn-circle"
				>
					<div class="indicator">
						<img alt="github" src="/github-mark-white.png" />
					</div>
				</a>
			</div>
		</div>
	</div>
</nav>
