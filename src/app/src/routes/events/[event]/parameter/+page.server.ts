import prisma from '$lib/server/prisma';
import { fail } from '@sveltejs/kit';
import { page } from '$app/stores';
import type { PageServerLoad } from './$types';

export const load = (async ({ params }) => {
	let param_event_id = parseInt(params.event);

	if (isNaN(param_event_id)) {
		return null;
	} else {
		const event_parameters = await prisma.event_parameters.findMany({
			where: {
				event_id: param_event_id
			}
		});

		const parameters = await prisma.parameters.findMany();
		const event = await prisma.events.findUnique({
			where: {
				id: param_event_id
			}
		});

		return { parameters: parameters, event: event };
	}
}) satisfies PageServerLoad;

export const actions = {
	load: async ({ cookies, request }) => {
		const data = await request.formData();

		try {
			const newEvent = await prisma.events.createMany({
				data: processInput(data.get('events'))
			});
		} catch (error) {
			return fail(422, {
				events: data.get('events'),
				error: error.message
			});
		}
	}
};
