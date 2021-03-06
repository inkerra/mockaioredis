'Generic Redis commands'


class GenericCommandsMixin:
    '''Generic commands mixin
    '''

    async def delete(self, key, *keys):
        '''Delete specified key(s)'''
        return self._redis.delete(key, *keys)


    async def exists(self, key, *keys):
        '''Check if key(s) exist

        Like in Redis 3.0.3+, returns int count of existing keys.
        If the same existing key is given multiple times, it is
        counted multiple times.
        '''
        all_keys = (key, ) + keys
        existing = 0
        # redis-py and, by extension mockredispy still only support
        # single-key checks that return True/False
        for k in all_keys:
            if self._redis.exists(k):
                existing += 1

        return existing

    async def set(self, *args, **kwargs):
        '''Set key'''
        if 'expire' in kwargs:
            kwargs['ex'] = kwargs.pop('expire')
            if not kwargs['ex']:
                kwargs['ex'] = None
        return self._redis.set(*args, **kwargs)

    def ping(self, *args, **kwargs):
        '''Ping server.'''
        return

    async def get(self, key):
        '''Get key(s)'''
        return self._redis.get(key)

    async def incr(self, key):
        '''Increment key'''
        return self._redis.incr(key)
