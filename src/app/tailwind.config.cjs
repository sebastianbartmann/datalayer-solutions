/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		minHeight: {
			25: '25vh',
			50: '50vh',
			60: '60vh',
			70: '70vh',
			full: '100vh'
		},
		extend: {}
	},
	plugins: [require('daisyui')],
	daisyui: {
		themes: ['dark', 'bumblebee', 'light', 'coffee']
	}
};
