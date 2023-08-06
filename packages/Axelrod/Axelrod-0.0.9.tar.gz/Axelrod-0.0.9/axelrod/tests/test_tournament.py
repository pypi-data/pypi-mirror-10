"""Tests for the main tournament class."""

import unittest
import axelrod
import logging
import multiprocessing


class TestTournament(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.game = axelrod.Game()
        cls.players = [
            axelrod.Cooperator(),
            axelrod.TitForTat(),
            axelrod.Defector(),
            axelrod.Grudger(),
            axelrod.GoByMajority()]
        cls.player_names = [str(p) for p in cls.players]
        cls.test_name = 'test'
        cls.test_repetitions = 5

        cls.expected_payoffs = [
            [600, 600, 0, 600, 600],
            [600, 600, 199, 600, 600],
            [1000, 204, 200.0, 204, 204],
            [600, 600, 199, 600.0, 600],
            [600, 600, 199, 600, 600]]

        cls.expected_outcome = [
            ('Cooperator', [1800, 1800, 1800, 1800, 1800]),
            ('Defector', [1612, 1612, 1612, 1612, 1612]),
            ('Go By Majority', [1999, 1999, 1999, 1999, 1999]),
            ('Grudger', [1999, 1999, 1999, 1999, 1999]),
            ('Tit For Tat', [1999, 1999, 1999, 1999, 1999])]
        cls.expected_outcome.sort()

    def test_init(self):
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            processes=4,
            noise=0.2)
        self.assertEqual(tournament.players, self.players)
        self.assertEqual(tournament.game.score(('C', 'C')), (3, 3))
        self.assertEqual(tournament.turns, 200)
        self.assertEqual(tournament.repetitions, 10)
        self.assertEqual(tournament.name, 'test')
        self.assertEqual(tournament._processes, 4)
        self.assertFalse(tournament.prebuilt_cache)
        self.assertIsInstance(tournament._logger, logging.Logger)
        self.assertIsInstance(tournament.result_set, axelrod.ResultSet)
        self.assertEqual(tournament.deterministic_cache, {})
        self.assertEqual(tournament.noise, 0.2)
        anonymous_tournament = axelrod.Tournament(players=self.players)
        self.assertEqual(anonymous_tournament.name, 'axelrod')

    def test_serial_play(self):
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions)
        scores = tournament.play().scores
        actual_outcome = sorted(zip(self.player_names, scores))
        self.assertEqual(actual_outcome, self.expected_outcome)

    def test_parallel_play(self):
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions,
            processes=2)
        scores = tournament.play().scores
        actual_outcome = sorted(zip(self.player_names, scores))
        self.assertEqual(actual_outcome, self.expected_outcome)

    def test_build_cache_required(self):
        # Noisy, no prebuilt cache, empty deterministic cache
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            processes=4,
            noise=0.2,
            prebuilt_cache=False)
        self.assertFalse(tournament._build_cache_required())

        # Noisy, with prebuilt cache, empty deterministic cache
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            processes=4,
            noise=0.2,
            prebuilt_cache=True)
        self.assertFalse(tournament._build_cache_required())

        # Not noisy, with prebuilt cache, deterministic cache has content
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            processes=4,
            prebuilt_cache=True)
        tournament.deterministic_cache = {'test': 100}
        self.assertFalse(tournament._build_cache_required())

        # Not noisy, no prebuilt cache, deterministic cache has content
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            processes=4,
            prebuilt_cache=False)
        tournament.deterministic_cache = {'test': 100}
        self.assertTrue(tournament._build_cache_required())

        # Not noisy, with prebuilt cache, empty deterministic cache
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            processes=4,
            prebuilt_cache=True)
        self.assertTrue(tournament._build_cache_required())

        # Not noisy, no prebuilt cache, empty deterministic cache
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            processes=4,
            prebuilt_cache=False)
        self.assertTrue(tournament._build_cache_required())

    def test_run_single_repetition(self):
        payoffs_list = []
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions)
        tournament._run_single_repetition(payoffs_list)
        self.assertEqual(len(payoffs_list), 1)
        self.assertEqual(payoffs_list[0], self.expected_payoffs)

    def test_run_serial_repetitions(self):
        payoffs_list = []
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions)
        tournament._run_serial_repetitions(payoffs_list)
        self.assertEqual(len(payoffs_list), self.test_repetitions)
        for r in range(self.test_repetitions):
            self.assertEqual(payoffs_list[r], self.expected_payoffs)

    def test_run_parallel_repetitions(self):
        payoffs_list = []
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions,
            processes=2)
        tournament._run_parallel_repetitions(payoffs_list)
        self.assertEqual(len(payoffs_list), self.test_repetitions)
        for r in range(self.test_repetitions):
            self.assertEqual(payoffs_list[r], self.expected_payoffs)

    def test_n_workers(self):
        max_processes = multiprocessing.cpu_count()

        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions,
            processes=1)
        self.assertEqual(tournament._n_workers(), max_processes)

        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions,
            processes=max_processes + 2)
        self.assertEqual(tournament._n_workers(), max_processes)

    @unittest.skipIf(
        multiprocessing.cpu_count() < 2,
        "not supported on single processor machines")
    def test_2_workers(self):
        # This is a separate test with a skip condition because we
        # cannot guarantee that the tests will always run on a machine
        # with more than one processor
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions,
            processes=2)
        self.assertEqual(tournament._n_workers(), 2)

    def test_start_workers(self):
        workers = 2
        work_queue = multiprocessing.Queue()
        done_queue = multiprocessing.Queue()
        for repetition in range(self.test_repetitions):
            work_queue.put(repetition)
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions)
        tournament._start_workers(workers, work_queue, done_queue)

        stops = 0
        while stops < workers:
            payoffs = done_queue.get()
            if payoffs == 'STOP':
                stops += 1
        self.assertEqual(stops, workers)

    def test_process_done_queue(self):
        workers = 2
        done_queue = multiprocessing.Queue()
        payoffs_list = []
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions)
        for r in range(self.test_repetitions):
            done_queue.put('test_payoffs')
        for w in range(workers):
            done_queue.put('STOP')
        tournament._process_done_queue(workers, done_queue, payoffs_list)
        self.assertEqual(len(payoffs_list), self.test_repetitions)
        for repetition in range(self.test_repetitions):
            self.assertEqual(payoffs_list[r], 'test_payoffs')

    def test_worker(self):
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions)

        work_queue = multiprocessing.Queue()
        for repetition in range(self.test_repetitions):
            work_queue.put(repetition)
        work_queue.put('STOP')

        done_queue = multiprocessing.Queue()
        tournament._worker(work_queue, done_queue)
        for r in range(self.test_repetitions):
            payoffs = done_queue.get()
            self.assertEqual(payoffs, self.expected_payoffs)
        queue_stop = done_queue.get()
        self.assertEqual(queue_stop, 'STOP')

    def test_play_round_robin_mutable(self):
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions)
        payoffs = tournament._play_round_robin()
        self.assertEqual(payoffs, self.expected_payoffs)
        self.assertTrue(
            (axelrod.Cooperator, axelrod.Defector) in
            tournament.deterministic_cache)

    def test_play_round_robin_immutable(self):
        tournament = axelrod.Tournament(
            name=self.test_name,
            players=self.players,
            game=self.game,
            turns=200,
            repetitions=self.test_repetitions)
        payoffs = tournament._play_round_robin(cache_mutable=False)
        self.assertEqual(payoffs, self.expected_payoffs)
        self.assertEqual(tournament.deterministic_cache, {})
