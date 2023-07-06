import prisma from '$lib/server/prisma';
import { fail } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load = (async () => {
	const response = await prisma.triggers.findMany();

	return { feed: response };
}) satisfies PageServerLoad;

function processInput(data) {
	try {
		const parsedJson = JSON.parse(data);
		return parsedJson;
	} catch (error) {
		const jsonArray = data.split(' ').map((word) => {
			return {
				name: word
			};
		});
		return jsonArray;
	}
}

export const actions = {
	batchCreate: async ({ cookies, request }) => {
		const data = await request.formData();

		try {
			const newEvent = await prisma.triggers.createMany({
				data: processInput(data.get('triggers'))
			});
		} catch (error) {
			return fail(422, {
				triggers: data.get('triggers'),
				error: error.message
			});
		}
	},
	deleteAll: async ({ cookies, request }) => {
		try {
			const newEvent = await prisma.triggers.deleteMany();
		} catch (error) {
			return fail(422, {
				error: error.message
			});
		}
	},

	create: async ({ cookies, request }) => {
		const data = await request.formData();

		console.log('data: ' + data.get('name'));

		try {
			const newEvent = await prisma.triggers.create({
				data: { name: data.get('name') }
			});
		} catch (error) {
			return fail(422, {
				name: data.get('name'),
				error: error.message
			});
		}
	},

	delete: async ({ cookies, request }) => {
		const data = await request.formData();

		try {
			const deletedEvent = await prisma.triggers.delete({
				where: {
					id: parseInt(data.get('id'), 10)
				}
			});
		} catch (error) {
			return fail(422, {
				name: data.get('name'),
				error: error.message
			});
		}
	}
};
