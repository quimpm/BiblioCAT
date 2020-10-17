collatz :: Int -> Int
collatz n = length $ takeWhile (/= 1) $ iterate f n
  where f s = if even s then s `div` 2 else s * 3 + 1

v :: Int
v = (* (-1)) . snd . maximum $ map f [1 .. 100000] where f x = (collatz x, -x)

main :: IO ()
main = print v
