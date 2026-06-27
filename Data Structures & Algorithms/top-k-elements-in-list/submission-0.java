
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (!map.containsKey(num)) {
                map.put(num, 1);
            } else {
                map.put(num, map.get(num) + 1);
            }
        }

        List<Integer> keys = new ArrayList<>(map.keySet());
        Collections.sort(keys, (a, b) -> map.get(b) - map.get(a));

        List<Integer> topK = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            topK.add(keys.get(i));
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = topK.get(i);
        }

        return result;
    }
}
