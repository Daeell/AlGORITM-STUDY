using System;
namespace boj
{
    public class Program
    {
        static void Main(string[] args)
        {
            string[] arg = Console.ReadLine().Split(" ");
            long n = long.Parse(arg[0]);
            long m = long.Parse(arg[1]);
            long k = long.Parse(arg[2]);
            long[] arr = new long[n];
            for (long i = 0; i < n; i++)
            {
                arr[i] = long.Parse(Console.ReadLine());
            }
            SegmentTree segmentTree = new SegmentTree(arr);
            for (long i = 0; i < m + k; i++)
            {
                string[] input2 = Console.ReadLine().Split(" ");
                long a = long.Parse(input2[0]);
                long b = long.Parse(input2[1]);
                long c = long.Parse(input2[2]);
                if (a == 1)
                {
                    segmentTree.Update(b - 1, c);
                }
                else
                {
                    Console.WriteLine(segmentTree.Sum(b - 1, c - 1));
                }
            }
        }
    }

    public class SegmentTree
    {
        private long[] tree;
        private long[] arr;
        public SegmentTree(long[] arr)
        {
            this.arr = arr;
            tree = new long[arr.Length * 4];
            Init(0, arr.Length - 1, 1);
        }

        private long Init(long start, long end, long node)
        {
            if (start == end)
            {
                return tree[node] = arr[start];
            }
            long mid = (start + end) / 2;
            return tree[node] = Init(start, mid, node * 2) + Init(mid + 1, end, node * 2 + 1);
        }

        public long Sum(long start, long end)
        {
            return Sum(start, end, 1, 0, arr.Length - 1);
        }

        private long Sum(long start, long end, long node, long left, long right)
        {
            if (start > right || end < left)
            {
                return 0;
            }
            if (start <= left && right <= end)
            {
                return tree[node];
            }
            long mid = (left + right) / 2;
            return Sum(start, end, node * 2, left, mid) + Sum(start, end, node * 2 + 1, mid + 1, right);
        }

        public void Update(long index, long value)
        {
            long diff = value - arr[index];
            arr[index] = value;
            Update(index, diff, 1, 0, arr.Length - 1);
        }

        private void Update(long index, long diff, long node, long left, long right)
        {
            if (index < left || index > right)
            {
                return;
            }
            tree[node] += diff;
            if (left != right)
            {
                long mid = (left + right) / 2;
                Update(index, diff, node * 2, left, mid);
                Update(index, diff, node * 2 + 1, mid + 1, right);
            }
        }
    }
}