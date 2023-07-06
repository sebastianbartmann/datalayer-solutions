<script lang="ts">
	import type { PageData } from './$types';
	import { enhance } from '$app/forms';
	import { DataHandler, Datatable, Th, ThFilter } from '@vincjo/datatables';

	export let form;
	export let data: PageData;

	let clipboardText = '';

	const handler = new DataHandler(data.feed, { rowsPerPage: 50 });
	const rows = handler.getRows();

	$: data, handler.setRows(data.feed);

	async function copyAllToClipboard() {
		try {
			await navigator.clipboard.writeText(JSON.stringify(data.feed));
			console.log('Text copied to clipboard');
		} catch (err) {
			console.error('Failed to copy text: ', err);
		}
	}

	async function copyNamesToClipboard() {
		const names = data.feed.map((item) => {
			return { name: item.name };
		});
		try {
			await navigator.clipboard.writeText(JSON.stringify(names));
			console.log('Text copied to clipboard');
		} catch (err) {
			console.error('Failed to copy text: ', err);
		}
	}

	async function readFromClipboard() {
		try {
			clipboardText = await navigator.clipboard.readText();
			console.log('Text read from clipboard:', clipboardText);
		} catch (err) {
			console.error('Failed to read text from clipboard: ', err);
		}
	}
</script>

<div class="bg-gray-100 w-full py-4">
	<div class="container mx-auto px-4 flex items-center">
		<h1 class="text-2xl font-semibold">Parameters</h1>
		<div class="flex">
			<button
				class="btn btn-sm rounded bg-secondary text-accent hover:bg-primary mx-1 ml-2"
				on:click={copyAllToClipboard}
			>
				copyAll
			</button>
			<button
				class="btn btn-sm rounded bg-secondary text-accent hover:bg-primary mx-1"
				on:click={copyNamesToClipboard}
			>
				copyNames
			</button>
			<button
				class="btn btn-sm rounded bg-secondary text-accent hover:bg-primary mx-1"
				on:click={readFromClipboard}
			>
				read
			</button>
			<form method="POST" action="?/deleteAll" use:enhance>
				<button class="btn btn-sm rounded bg-secondary text-accent hover:bg-primary mx-1">
					deleteAll
				</button>
			</form>
		</div>
	</div>
	<div class="container mx-auto flex items-center text-red-400">
		{#if form?.error}
			<p class=" error">{form.error}</p>
		{/if}
	</div>
</div>
<div class="w-full min-h-screen bg-gray-100">
	<div class="container mx-auto px-4 py-6 flex">
		<!-- Left column -->
		<div class="w-1/2 bg-white p-4 rounded shadow">
			<div class=" flex flex-col justify-center">
				<table class="table-auto">
					<thead>
						<tr>
							<th />
							<Th {handler} orderBy="id">ID</Th>
							<Th {handler} orderBy="name">Name</Th>
						</tr>
						<tr>
							<th />
							<ThFilter {handler} filterBy="id" />
							<ThFilter {handler} filterBy="name" />
						</tr>
					</thead>
					<tbody>
						{#each $rows as row}
							<tr>
								<td>
									<form method="POST" action="?/delete" use:enhance>
										<input
											value={row.id}
											class="border"
											hidden
											required
											name="id"
											autocomplete="off"
										/>
										<button
											class="btn btn-xs rounded bg-red-500 text-accent hover:bg-primary"
											name="batchCreate"
										>
											del
										</button>
									</form>
								</td>
								<td>{row.id}</td>
								<td>{row.name}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>

		<!-- Right column -->
		<div class="w-1/2 bg-white p-4 rounded shadow ml-4">
			<div class="card">
				<div class="card-body">
					<h2 class="card-title">Create a parameter</h2>

					<form method="POST" action="?/create" use:enhance>
						<label>
							add a parameter:
							<input
								value={form?.name ?? ''}
								class="border"
								required
								name="name"
								autocomplete="off"
							/>
						</label>

						<div class="card-actions my-2">
							<button
								class="btn btn-sm rounded bg-secondary text-accent hover:bg-primary"
								name="batchCreate"
							>
								Create
							</button>
						</div>
					</form>
					<div>{clipboardText}</div>
				</div>
			</div>

			<div class="card">
				<div class="card-body">
					<h2 class="card-title">Batch create parameters</h2>
					<form method="POST" action="?/batchCreate" use:enhance>
						<label>
							parameters:
							<input class="border" required name="parameters" autocomplete="off" />
						</label>
						<br />
						<div class="card-actions my-2">
							<button
								class="btn btn-sm rounded bg-secondary text-accent hover:bg-primary"
								name="batchCreate"
							>
								batch Create
							</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</div>
