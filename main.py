import multiprocessing as mp
import subprocess
import discord_bot_program
import search_query_program

def discord_bot_process(queue):
    discord_bot_program.run_discord_bot(queue)

def search_query_process(queue):
    search_query_program.search_query_process(queue)

if __name__ == '__main__':
    # Create a multiprocessing queue
    queue = mp.Queue()

    # Start the Discord bot process
    discord_bot_proc = mp.Process(target=discord_bot_process, args=(queue,))
    discord_bot_proc.start()

    # Start the search query process
    search_query_proc = mp.Process(target=search_query_process, args=(queue,))
    search_query_proc.start()

    # Wait for both processes to finish
    discord_bot_proc.join()
    search_query_proc.join()
