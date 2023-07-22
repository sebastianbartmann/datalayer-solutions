<script>
	function handleClick() {
		my_modal_3.showModal();
	}
</script>

<!-- You can open the modal using ID.showModal() method -->
<button class="btn" on:click={handleClick}>open modal</button>
<!-- You can open the modal using ID.showModal() method -->
<dialog id="my_modal_3">
	<h3 class="font-bold text-lg">Hello!</h3>
	<p class="py-4">Press ESC to close</p>
</dialog>
