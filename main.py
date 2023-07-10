from create_bot import dp
from aiogram import executor
from modules import key, ttk_test

key.register_handlers_key(dp)
ttk_test.register_handlers_ttk(dp)

executor.start_polling(dp, skip_updates=True)



